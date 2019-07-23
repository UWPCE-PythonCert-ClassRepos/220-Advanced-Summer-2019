'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging
from datetime import datetime

# LOG_FILE = "charges_calc_{today}.log".format(today=datetime.today().strftime("%Y_%M_%D"))
# LOG_FILE = "charges_calc_.log"


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='show debug messages', required=False, type=int, choices=[0, 1, 2, 3])

    return parser.parse_args()


def set_logging_level(level=0):
    """
    0: No debug messages or log file.
    1: Only error messages.
    2: Error messages and warnings.
    3: Error messages, warnings and debug messages.
    """
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    LOG_FILE = "charges_calc.log"

    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(LOG_FILE, mode='a+')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if level == 3:
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.DEBUG)
    elif level == 2:
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.WARNING)
    elif level == 1:
        file_handler.setLevel(logging.ERROR)
        console_handler.setLevel(logging.ERROR)
    else:  # "0" or none
        file_handler.setLevel(logging.CRITICAL)
        console_handler.setLevel(logging.CRITICAL)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    print(logger.debug("logging level selected: {level}".format(level=level)))


def load_rentals_file(filename):

    with open(filename) as file:
        try:
            data = json.load(file)
            logging.debug(f"loading {filename}")

        except Exception:
            logging.error("An exception encountered loading json file")
            exit(0)
    return data


def calculate_additional_fields(data):
    for key, value in data.items():
        logging.debug(f"calculating additional fields on {data.items()}")
        try:
            if value["rental_start"] == "" or value["rental_end"] == "":
                continue
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            value['total_days'] = abs((rental_end - rental_start).days)
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except Exception:
            logging.error("An exception at calculating additional fields")
            exit(0)

    return data


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    set_logging_level(args.debug)

    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
