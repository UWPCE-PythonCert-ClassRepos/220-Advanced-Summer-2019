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


# logging details
log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
log_file = datetime.datetime.now().strftime('%Y-%m-%d')+’.log’

formatter = logging.Formatter(log_format)
file_handler = logging.FileHandler(log_file)
logger = logging.getLogger()
logger.addHandler(file_handler)

# set a new debug arguement to set the level


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)

    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
        except:
            # Add logging here
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
            # Add logging here
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

