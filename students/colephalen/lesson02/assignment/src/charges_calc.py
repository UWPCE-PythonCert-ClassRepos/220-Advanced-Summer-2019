'''
Returns total price paid for individual rentals 
'''
import argparse
import json
import datetime
import math

import logging  # in class 7/16


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=False, default='source.json')  #
    parser.add_argument('-o', '--output', help='output JSON file', required=False, default='output.json')

    parser.add_argument('-d', '--debug', help='set logging level', required=False)  # added in class 7/16

    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
        except Exception as e:
            print(e)
            exit(0)
    return data


def calculate_additional_fields(data):
    out = []
    for key, value in data.items():
        try:
            if value["rental_start"] == "" or value["rental_end"] == "":
                logging.debug('one of the dates fields is empty')
                continue
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')

            value['total_days'] = abs((rental_end - rental_start).days)

            if rental_start > rental_end:
                logging.error('for key: {} the end date of {} occurs before the start date of {}'
                              .format(key, rental_end, rental_start))

            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])

            if value['total_days'] < 0:
                continue

            if value['units_rented'] == 0:
                continue

            value['unit_cost'] = value['total_price'] / value['units_rented']

            out.append(value)

        except Exception as e:
            print(value)
            print(e)
            exit(0)

    return out


def set_logging_level(level=0):  # in class 7/16

    """
    0: No debug messages or log file.

    1: Error (stream and file)

    2: Error messages (stream and file) and warnings (stream and file).

    3: Error messages (stream and file), warnings (stream and file) and debug messages (stream).
    """
    LOG_FILE = "changes_calc.log"
    logger = logging.getLogger()
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(LOG_FILE)  # file handler
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if level == "3":
        file_handler.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.DEBUG)
    elif level == "2":
        file_handler.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.WARNING)
    elif level == "1":
        file_handler.setLevel(logging.ERROR)
        stream_handler.setLevel(logging.ERROR)
    else:  # "0" or None
        file_handler.setLevel(logging.CRITICAL)
        stream_handler.setLevel(logging.CRITICAL)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    args = parse_cmd_arguments()

    set_logging_level(args.debug)  # in class 7/16

    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)

    logging.debug('debug')
    logging.info('logging info')
    logging.error('loggin error')
    logging.warning('warning')
    logging.critical('critical')

