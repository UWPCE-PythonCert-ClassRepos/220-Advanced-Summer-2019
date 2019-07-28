'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging

def parse_cmd_arguments():
    """
    creates an argument parser, adds 3 arguments
    i for input, o for output and optional d for debugging with 3 levels
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='level of debug, 0 is default = not set, 1 = critical, 2 = warning, 3 = debug', required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    """
    Opens JSON file and returns data,
    logs a critical error if there is an error
    """
    with open(filename) as file:
        try:
            data = json.load(file)
            #Json decode error, expecting property name enclosed in double quotes
        except Exception as exception:
            logging.critical(f'Unable to load json file with name {filename} due to {exception}')
    return data

def calculate_additional_fields(data):
    """
    Takes data and iterates through the keys/values
    series of try, except blocks that will log an error if something occurs
    converts rental start/end to datetime
    if the total days is negative: it will switch the start/end days and recalculate total days logging this only if level 3 (debug logging level)
    
    Generally the switch in the rental start/end would be a warning level debug for me, 
    for this exercise I made it a debug level due to there being so many of them
    and it clogging up the log. I would write a program to fix the data in the source.json if I was to continue
    """
    for key, value in data.items():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
        except Exception as exception:
            logging.warning(f'FAILED - rental start/rental end {key} with exception {exception}')
        try:
            value['total_days'] = (rental_end - rental_start).days
            if value['total_days'] < 0:
                logging.debug(f'total days is negative, switching rental start and end for {key}')
                foo = rental_start
                rental_start = rental_end
                rental_end = foo
                value['total_days'] = (rental_end - rental_start).days
        except Exception as exception:
            logging.warning(f'could not update total days for {key} with exception {exception}')
        try:
            value['total_price'] = value['total_days'] * value['price_per_day']
            logging.debug(f'total price for {key} is {value["total_price"]}')
        except Exception as exception:
            logging.warning(f"FAILED - total price {key} with exception {exception}")
        try:
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
        except Exception as exception:
            logging.warning(f"FAILED - sqrt total price - {key} with exception {exception}")
        try:
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except Exception as exception:
            logging.warning(f"FAILED - unit cost {key} with exception {exception}")
    return data

def save_to_json(filename, comp_data):
    """
    opens a json file (overwrites the previous one)
    dumps the completed data into this json file
    """
    if '.json' not in filename:
        filename = f'{filename}.json'
    with open(filename, 'w') as file:
        json.dump(comp_data, file)


def setup_logger(level='0'):
    """
    sets up a logger with an optional level taken from the args parser
    sets both a file_handler and a console handler
    if level is 0 or not changed, logging is disabled
    if level = 1: Critical, Level = 2: Warning, Level = 3: Debug
    """
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

    log_file_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'

    logger = logging.getLogger()

    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if level == '0' or not level:
        logger.disabled = True
    elif level == '1':
        console_handler.setLevel(logging.CRITICAL)
        file_handler.setLevel(logging.CRITICAL)
        logger.setLevel(logging.CRITICAL)
    elif level == '2':
        console_handler.setLevel(logging.WARNING)
        file_handler.setLevel(logging.WARNING)
        logger.setLevel(logging.WARNING)
    elif level == '3':
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)


    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

if __name__ == "__main__":
    args = parse_cmd_arguments()
    setup_logger(args.debug)
    logging.debug(f'logger set up with level {args.debug}')
    data = load_rentals_file(args.input)
    logging.debug(f'data gathered from JSON file {args.input}')
    data = calculate_additional_fields(data)
    logging.debug('calculation run on data')
    save_to_json(args.output, data)
    logging.debug(f'new json data saved to {args.output}')
