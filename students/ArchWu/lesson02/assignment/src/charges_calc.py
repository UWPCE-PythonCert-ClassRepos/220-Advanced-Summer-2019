'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
FILE_HANDLER = logging.FileHandler(LOG_FILE)
FORMATTER = logging.Formatter(LOG_FORMAT)
#LEVEL = {0: logging.NOTSET, 1:logging.ERROR, 2:logging.WARNING, 3:logging.INFO}
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(FORMATTER)
LOGGER = logging.getLogger()
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)

def parse_cmd_arguments():
    """Command Parser"""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='debug option',
                        required=False, type=int, default=0)
    return parser.parse_args()

def load_rentals_file(filename):
    """File loader"""
    file = open(filename, 'r')
    try:
        data = json.load(file)
        logging.info("Data loading Hajime")
        return data
    except json.decoder.JSONDecodeError:
        exit(0)
    return -1

def calculate_additional_fields(data):
    """Calculator"""
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'],
                                                      '%m/%d/%y')
            if not rental_start:
                logging.warning("Missing rental start date!")
            rental_end = datetime.datetime.strptime(value['rental_end'],
                                                    '%m/%d/%y')
            if not rental_end:
                logging.warning("Missing rental end date!")
            value['total_days'] = abs((rental_end - rental_start).days)
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except ValueError:
            logging.error("Something's not quite right! %s", value)
            continue
        except ZeroDivisionError:
            logging.error("Divided by zero")
            continue
    return data

def save_to_json(filename, data):
    """File Saver"""
    with open(filename, 'w') as file:
        json.dump(data, file)

def choose_debug_lvl(arg):
    """Debug Level Chooser"""
    if arg == 0:
        LOGGER.setLevel(0)
    elif arg == 1:
        LOGGER.setLevel(logging.ERROR)
    elif arg == 2:
        LOGGER.setLevel(logging.WARNING)
    elif arg == 3:
        LOGGER.setLevel(logging.NOTSET)
    else:
        logging.error("Error setting logging level %s", arg)

if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    choose_debug_lvl(ARGS.debug)
    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(ARGS.output, DATA)
    logging.info('All Done!')
    logging.warning("Just a test warning")
