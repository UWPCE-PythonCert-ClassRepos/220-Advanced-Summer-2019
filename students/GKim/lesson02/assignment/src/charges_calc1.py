'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging


def parse_cmd_arguments():
    # This method is used for taking a json file as an input (source.json)
    # and spitting out a json file output (name you choose)
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    logging.debug("Input file has been set")
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('d', '--debug', help='set logging level', required=False)
    logging.debug("Output file has been file")
    return parser.parse_args()


def load_rentals_file(filename):
    # This method is used to read a json file which initially gets read as a text file
    # so we use the json library to put it back into a json object
    with open(filename) as file:
        try:
            data = json.load(file)
            logging.debug("Success, json has been loaded")
        except FileNotFoundError:
            logging.error("File does not exist")
            exit(0)
    return data


def calculate_additional_fields(data):

    output =[]

    for key, value in data.items():
        try:
            if value["rental_start"] == "" or value["rental-end"] == "":
                continue

            logging.debug(value)
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            value['total_days'] = abs((rental_end - rental_start).days)
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']

            value["key"] = key
            output.append()

        except ZeroDivisionError:
            logging.error("Zero Rented Units, cannot divide by zero.")
            value['unit_cost'] = "Cannot compute"
        except:
            logging.error(value)
            exit(0)
    return data


def set_logging_level(level=0):
    """
    0: Nothing
    1: Error (stream+file)
    2: Error (stream+file) and warnings (stream + file)
    3: Error (stream+file) and warnings (stream + file) and debug (stream)
    """
    LOG_FILE = "charges_calc.log"
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)-4d\t%(message)s"
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(LOG_FILE)
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
    else: #"0" or None
        file_handler.setLevel(logging.CRITICAL)
        stream_handler.setLevel(logging.CRITICAL)

    # logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.debug("logging level selected: {level}".format(level=level))

def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    # You can change the filter here to warning if you want
    logging.getLogger().setLevel("WARNING")
    args = parse_cmd_arguments()
    set_logging_level(args.debug)
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)

