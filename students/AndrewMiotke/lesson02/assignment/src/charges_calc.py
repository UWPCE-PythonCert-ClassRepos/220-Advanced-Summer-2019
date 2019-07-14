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

# Logging layout
LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
FORMATTER = logging.Formatter(LOG_FORMAT)
FILE_HANDLER = logging.FileHandler('charges_calc.log')

# Error
ERROR_LOGGER = FILE_HANDLER
ERROR_LOGGER = logging.getLogger()
ERROR_LOGGER.addHandler(FILE_HANDLER)

# Warning
WARNING_LOGGER = FILE_HANDLER
WARNING_LOGGER = logging.getLogger()
WARNING_LOGGER.addHandler(FILE_HANDLER)

# DEBUG
DEBUG_LOGGER = FILE_HANDLER
DEBUG_LOGGER = logging.getLogger()
DEBUG_LOGGER.addHandler(FILE_HANDLER)
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)


def parse_cmd_arguments():
    """ Command line arguements to start the program """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d1', '--debug1', action='store_true', help='debug error messages')
    parser.add_argument('-d2', '--debug2', action='store_true', help='debug error and warning messages')
    parser.add_argument('-d3', '--debug3', action='store_true', help='Shows error, warnings, and debug messages')

    return parser.parse_args()


def load_rentals_file(filename):
    """ Load the source.json file """
    with open(filename) as file:
        try:
            parsed_json = file.read()
            parsed_json = parsed_json.replace(',,', ',')
            data = json.loads(parsed_json)
        except ValueError:
            logging.warning("Exiting: load_rentals_file()")
            exit(0)
    return data


def calculate_additional_fields(data):
    """ Calculates any other fields for json """
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value["rental_start"], "%m/%d/%y")
            rental_end = datetime.datetime.strptime(value["rental_end"], "%m/%d/%y")
            value["total_days"] = (rental_end - rental_start).days
            value["total_price"] = value["total_days"] * value["price_per_day"]
            value["sqrt_total_price"] = math.sqrt(value["total_price"])
            value["unit_cost"] = value["total_price"] / value["units_rented"]
        except ValueError:
            ERROR_LOGGER.error("Exiting: calculate_additional_fields()")
            exit(0)

    return data


def save_to_json(filename, data):
    """ Saves the filename with new data to json """
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    # use args debug and handle the logging
    args = parse_cmd_arguments()
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
