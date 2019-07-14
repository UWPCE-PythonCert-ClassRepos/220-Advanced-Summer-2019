'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging


"""
NOTES FROM CLASS - DELETE THESE LATER
Create 2 file handlers
Create a if/elif statement for each logging level
"""

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

FORMATTER = logging.Formatter(LOG_FORMAT)

# DEBUG
FILE_HANDLER = logging.FileHandler('charges_calc.log')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)

# Warning
WARNING_HANDLER = logging.FileHandler('charges_calc.log')
WARNING_HANDLER.setLevel(logging.WARNING)
WARNING_HANDLER.setFormatter(FORMATTER)

# Error
ERROR_HANDLER = logging.FileHandler('charges_calc.log')
ERROR_HANDLER.setLevel(logging.ERROR)
ERROR_HANDLER.setFormatter(FORMATTER)


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d1', '--debug1', action='store_true', help='debug error messages')
    parser.add_argument('-d2', '--debug2', action='store_true', help='debug error and warning messages')
    parser.add_argument('-d3', '--debug3', action='store_true', help='Shows error, warnings, and debug messages')

    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            # s needs a better variable name
            s = file.read()
            s = s.replace(',,', ',')
            data = json.loads(s)
        except ValueError:
            logging.warning("Exiting: load_rentals_file()")
            exit(0)
    return data


def calculate_additional_fields(data):
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value["rental_start"], "%m/%d/%y")
            rental_end = datetime.datetime.strptime(value["rental_end"], "%m/%d/%y")
            value["total_days"] = (rental_end - rental_start).days
            value["total_price"] = value["total_days"] * value["price_per_day"]
            value["sqrt_total_price"] = math.sqrt(value["total_price"])
            value["unit_cost"] = value["total_price"] / value["units_rented"]
        except:
            logging.error("Exiting: calculate_additional_fields()")
            exit(0)

    return data


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    # use args debug and handle the logging
    args = parse_cmd_arguments()
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)

