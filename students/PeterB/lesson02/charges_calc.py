#!/usr/bin/env python3
'''
Returns total price paid for individual rentals 
'''
import argparse
import datetime
import json
import math
import logging


def init_logger(level):
    '''sets logger'''
    # convert string to int for log level
    level = int(level)
    LOG_FILE = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
    # format log
    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)-4d\t%(message)s"


    # attach formatter
    formatter = logging.Formatter(log_format)

    # add file handler to log file
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # add console to handler

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # add handlers to logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # 0 = no debug message
    if level == 0:
        #logger.setLevel(logging.CRITICAL)
        stream_handler.setLevel(logging.CRITICAL)
        file_handler.setLevel(logging.CRITICAL)

    if level == 1:
        #logger.setLevel(logging.ERROR)
        stream_handler.setLevel(logging.ERROR)
        file_handler.setLevel(logging.ERROR)

    if level == 2:
        #logger.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.ERROR)
        file_handler.setLevel(logging.WARNING)

    if level == 3:
        #logger.setLevel(logging.CRITICAL)
        stream_handler.setLevel(logging.WARNING)
        file_handler.setLevel(logging.DEBUG)

  #  logger.setLevel(logging.DEBUG)
  #  logger.addHandler(file_handler)
  #  logger.addHandler(stream_handler)


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='output JSON file', required=True)
    parser.add_argument('-d', '--debug', help='set logging level', required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
        except Exception as exception:
            logging.critical(f'Unable to load json file with name {filename} due to {exception}')
        return data

    # with open(filename, 'r') as file:
    #     loaded_json_data = json.load(file)
    #     try:
    #         data = json.load(file)
    #         return data
    #     except Exception as exception:
    #         logging.error(exception)
    #         logging.debug('type: {}, {}'.format(type(d), len(d)))
    # exit(-1)
    # return loaded_json_data

def calculate_additional_fields(data):

    for key, value in data.items():
        try:
            if value["rental_start"] == "" or value["rental_end"] == "":
                #logging
                continue
            rental_start = datetime.datetime.strptime(value["rental_start"], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value["rental_end"], '%m/%d/%y')
            value["total_days"] = abs((rental_end - rental_start).days)
            if total_days <= 0:
                raise ValueError('Can not end before start')
            value["total_price"] = value["total_days"] * value["price_per_day"]
            value["sqrt_total_price"] = math.sqrt(value["total_price"])
            value["unit_cost"] = value["total_price"] / value["charges_calc.py -i source -o output -d calc_logunits_rented"]

        except ValueError as ex:
            if "time data '' doesnt match format" in str(ex):
                logging.warning('no rental_end for rental %s', value)
            elif "math domain error" in str(ex):
                logging.warning('total_price is negative %s: %s', value, data[value]['total_price'])
            elif "does not match format" in str(ex):
                logging.warning(err)
            elif 'Can not end before start' in str(ex):
                logging.warning('invalid length of rental %s', value)
            exit(0)

            value["key"] = key

        except:
            exit(0)
    return data

def save_to_json(filename, data_store):
    if '.json' not in filename:
        filename = f'{filename}.json'
    with open(filename, 'w') as file:
        json.dump(data_store, file)

    # if filename:
    #     with open(filename, 'w') as f:
    #         json.dump(data_store, f)

if __name__ == "__main__":
    args = parse_cmd_arguments()
    # init_logger(args.debug)
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
