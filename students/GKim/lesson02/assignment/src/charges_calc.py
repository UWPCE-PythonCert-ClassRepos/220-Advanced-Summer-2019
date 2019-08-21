
"""
Returns total price paid for individual rentals
"""
import argparse
import json
import datetime
import math
import logging


# LOGGING SETTING START
LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d")+'charges_calc.log'
FORMATTER = logging.Formatter(LOG_FORMAT)
DICT_LEVEL = {'0': 'disabled', '1': 'ERROR', '2': 'WARNING', '3': 'DEBUG'}

# Log setting for writing to file
FILE_HANDLER = logging.FileHandler(LOG_FILE)
FILE_HANDLER.setLevel(logging.WARNING)
FILE_HANDLER.setFormatter(FORMATTER)

# Log setting for display to standout.
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setLevel(logging.DEBUG)  # Send log to console: DEBUG level
CONSOLE_HANDLER.setFormatter(FORMATTER)

LOGGER = logging.getLogger()
# LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)
# LOGGING SETTING END!


def parse_cmd_arguments():
    """
    This function to return arguments:
        Input json file.
        Output json file.
        Log level.
    Usage: -i ./source.json -o ./out.json -d DEBUG
    """
    logging.debug("Enter parse cmd argument routine!")
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', choices=DICT_LEVEL, help='Usage: -d 0. \
                        Level: 0: OFF, 1: ERROR, 2: WARNING, 3: DEBUG', 
                        default=2, required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    """ This function is to load the jason data file. """
    # logger = logging.getLogger('JASON.LOAD')
    try:
        with open(filename, 'r') as file:
            try:
                logging.debug("Begin Loading jason file: %s.", filename)
                data = json.load(file)
                # Got this error when run debug:
                # json.decoder.JSONDecodeError: ...:
                # line 5884 column 23 (char 130093)
            except json.JSONDecodeError as error_1:
                logging.error("File: invalid JSON syntax! Please fix: %s", error_1)
                exit(1)
    except FileNotFoundError as error_2:  # Some othe errors
        logging.error("File error: %s", error_2)
        exit(2)

    return data


def calculate_additional_fields(data):
    """
    What does this do?  Update the "data" with additional data then
    return "data" set.
    """
    # logger = logging.getLogger('JASON.CALC')
    logging.debug("Entering calculation additional field routine!")
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'],
                                                      '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'],
                                                    '%m/%d/%y')

            # Error: Used for inconsistencies in the source data that will
            # cause the script to crash or report incorrect results. Shown
            # on screen and on the log file.
            if rental_start >= rental_end:
                logging.error("start_date >= end_date - inconsistencies: %s", value)
                # raise ValueError
            else:
                value['total_days'] = (rental_end - rental_start).days
                value['total_price'] = value['total_days'] * value['price_per_day']
                value['sqrt_total_price'] = math.sqrt(value['total_price'])
                value['unit_cost'] = value['total_price'] / value['units_rented']
        except ValueError as error_1:
            logging.error('Value set in json has error: %s. DATA: %s ', error_1, value)
            continue  # Go to next record on the try.
        #  Catch - keyError: ie 'priceq_per_day'
        except KeyError as warning_1:
            logging.warning('Missing value or has KeyError: %s, %s', warning_1, value)
            continue
        except ZeroDivisionError as error_2:
            logging.error("Devide by zero.  Check 'units_rent': %s, %s", error_2, value)
            continue

    return data


def save_to_json(filename, data):
    """To save the Jason output file."""
    # logger = logging.getLogger('JASON.SAVE_OUT')
    with open(filename, 'w') as file:
        logging.debug("writing to file: %s", filename)
        json.dump(data, file, sort_keys=True, indent=4)  # Prettyprint


if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    if ARGS.debug == '0':
        LOGGER.disabled = True
    else:
        # logging.basicConfig(level=(DICT_LEVEL.get(ARGS.debug, 'WARNING')))
        LEVEL = DICT_LEVEL.get(ARGS.debug, 'WARNING')
        LOGGER.setLevel((LEVEL))
    LOGGER.debug("Command in - File input: %s. File output: %s. Log level: %s. \
                 debug value: %s.", ARGS.input, ARGS.output, ARGS.debug,
                 DICT_LEVEL.get(ARGS.debug, 'WARNING'))

    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(ARGS.output, DATA)