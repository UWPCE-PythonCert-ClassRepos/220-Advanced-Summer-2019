'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging
import pdb

log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter(log_format)
#LEVEL = {1:logging.ERROR, 2:logging.WARNING, 3:logging.INFO}
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
LOGGER = logging.getLogger()
LOGGER.addHandler(file_handler)
LOGGER.addHandler(console_handler)

def parse_cmd_arguments():
    """Command Parser"""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='debug option', required=True, type=int)
    return parser.parse_args()


def load_rentals_file(filename):
    """File loader"""
    file = open(filename, 'r')
    try:
        data = json.load(file)
        logging.info("Data loading Hajime")
        return data
    except json.decoder.JSONDecodeError as e:
        exit(0)
    return -1

def calculate_additional_fields(data):
    """Calculator"""
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            if not rental_start:
                logging.warning("Missing rental start date!")
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            if not rental_end:
                logging.warning("Missing rental end date!")
            value['total_days'] = (rental_end - rental_start).days
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except ValueError:
            logging.error("Something's not quite right! {}".format(value))
            continue
        except:
            logging.error("Wierd thing happens")
            exit(0)
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
        logging.error("Error setting logging level {}".format(arg))

if __name__ == "__main__":
    args = parse_cmd_arguments()
    choose_debug_lvl(args.debug)
    DATA = load_rentals_file(args.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(args.output, DATA)
    logging.info('All Done!')
    logging.warning("Just a test warning")
