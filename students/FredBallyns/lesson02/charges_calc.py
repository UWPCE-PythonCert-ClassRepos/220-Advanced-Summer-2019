#!/usr/bin/env python3
'''
Returns total price paid for individual rentals
'''

import argparse
import json
import datetime
import math
import logging


def parse_cmd_arguments():
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-i', '--input', help='input JSON file', required=True)
        parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
        parser.add_argument('-d', '--debug', help='set logging level: 0 default for disabled, 1 errors, 2 for warnings, 3 for debug', required=False, default="0")
        print("Input Arguments Received")
        return parser.parse_args()
    except Exception as exception:
        print(f"Invalid Arguments. {exception}")


def set_logging_level(level='0'):
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"

    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger()
    if level == "3":
        file_handler.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    elif level == "2":
        file_handler.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.WARNING)
        logger.setLevel(logging.WARNING)
    elif level == "1":
        file_handler.setLevel(logging.ERROR)
        stream_handler.setLevel(logging.ERROR)
        logger.setLevel(logging.ERROR)
    else:
        logger.disabled = True
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logging.debug(f'Logger set to level {level}')


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
            logging.debug(f"File loaded {filename}")
        except Exception as exception:
            logging.error(f'Unable to load json file with name {filename} due to {exception}')
    return data


def calculate_additional_fields(data):
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
        except Exception as exception:
            logging.warning(f"Failed to get Rental Start due to {exception}")
            continue

        try:
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
        except Exception as exception:
            logging.warning(f"Failed to get Rental End. May have not been returned yet. {exception}")
            continue

        try:
            value['total_days'] = (rental_end - rental_start).days
            if value['total_days']<0:
                logging.error(f"End before start. Assuming dates entered backwards")
                rental_end, rental_start = rental_start, rental_end
                value['total_days'] = (rental_end - rental_start).days
        except Exception as exception:
            logging.warning(f"Failed to calculate total days. {exception}")
            continue

        try:
            value['total_price'] = value['total_days'] * value['price_per_day']
        except Exception as exception:
            logging.warning(f"Failed to calculate total price. {exception}")
            continue

        try:
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
        except Exception as exception:
            logging.warning(f"Failed to calculate sqrt total price. {exception}")
            continue

        try:
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except Exception as exception:
            logging.warning(f"Failed to calculate unit cost. {exception}")
    return data


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)
        logging.debug(f'Data saved to file {filename}')


if __name__ == "__main__":
    args = parse_cmd_arguments()
    set_logging_level(args.debug)
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)