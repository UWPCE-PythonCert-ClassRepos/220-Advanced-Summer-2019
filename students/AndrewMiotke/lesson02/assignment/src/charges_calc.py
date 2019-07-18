'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging

def parse_cmd_arguments():
    """ Command line arguements to start the program """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='debug error messages', required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    """ Load the source.json file """
    with open(filename) as file:
        try:
            parsed_json = file.read()
            parsed_json = parsed_json.replace(',,', ',')
            data = json.loads(parsed_json)
        except ValueError:
            logging.error(ValueError)
            exit(0)
    return data


def calculate_additional_fields(data):
    """ Calculates any other fields for json """
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value["rental_start"], "%m/%d/%y")
        except ValueError:
            # add logging
            logging.error(ValueError)
            rental_end = datetime.datetime.strptime(value["rental_end"], "%m/%d/%y")
            value["total_days"] = (rental_end - rental_start).days
            value["total_price"] = value["total_days"] * value["price_per_day"]
            value["unit_cost"] = value["total_price"] / value["units_rented"]
            value["sqrt_total_price"] = math.sqrt(value["total_price"])
        except ValueError:
            logging.error(ValueError)
            raise

    return data


def save_to_json(filename, data):
    """ Saves the filename with new data to json """
    with open(filename, 'w') as file:
        json.dump(data, file)


def debug_levels(level=0):
    LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'

    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    FORMATTER = logging.Formatter(LOG_FORMAT)

    FILE_HANDLER = logging.FileHandler(LOG_FILE)
    FILE_HANDLER.setFormatter(FORMATTER)

    STREAM_HANDLER = logging.StreamHandler(LOG_FILE)
    STREAM_HANDLER.setFormatter(FORMATTER)

    if level == "3":
        FILE_HANDLER.setLevel(logging.WARNING)
        STREAM_HANDLER.setLevel(logging.DEBUG)
    elif level == "2":
        FILE_HANDLER.setLevel(logging.WARNING)
        STREAM_HANDLER.setLevel(logging.WARNING)
    elif level == "1":
        FILE_HANDLER.setLevel(logging.ERROR)
        STREAM_HANDLER.setLevel(logging.ERROR)
    else:
        FILE_HANDLER.setLevel(logging.NOTSET)
        STREAM_HANDLER.setLevel(logging.NOTSET)

    logger.addHandler(FILE_HANDLER)
    logger.addHandler(STREAM_HANDLER)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    debug_levels(args.debug)
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
