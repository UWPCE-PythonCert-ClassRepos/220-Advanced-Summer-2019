"""
Returns total price paid for individual rentals
"""
import argparse
import json
import datetime
import math
import logging


def parse_cmd_arguments():
    """
    creates an argument parser for the program
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='[3: ERROR, 2: WARN, 1: DEBUG, 0: NONE (default)]',
                        required=False, type=int, default=0)

    return parser.parse_args()


def load_rentals_file(filename):
    """
    Opens JSON file and returns data,
    logs a critical error if there is an error
    """
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError as exception:
        # Log exception if unable to open file
        logging.critical(f'Unable to open file {filename} due to:\n\t{exception}')
        exit(1)


def calculate_additional_fields(cal_data):
    """
    Calculate the following additional field from the input data
        1. total_days as total number of rental days
        2. total_price as total price of the rental
        3. sqrt_total_price as square root of the rental
        4. unit_cost as in unit cost of the rental
    :param cal_data: the input data
    :return: updated data
    """
    for key, value in cal_data.items():
        logging.debug('*' * 10 + f' Computing for {key} ' + '*' * 10)
        # Update total days
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            logging.debug(f'Rental start time {rental_start}')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            logging.debug(f'Rental end time {rental_end}')

            # If start data is after end date flip the entry
            total_days = (rental_end - rental_start).days
            if total_days < 0:
                logging.debug(f'Start date after end date, hence flipping dates')
                total_days = -total_days
            value['total_days'] = total_days
            logging.debug(f'Rental total days {total_days}')

            value['total_price'] = total_days * value['price_per_day']
            logging.debug(f'Rental total price {value["total_days"]}')

            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            logging.debug(f'Rental square root of total price {value["total_days"]}')

            value['unit_cost'] = value['total_price'] / value['units_rented']
            logging.debug(f'Rental unit cost {value["rental_start"]}')

        except Exception as exception:
            # Log the warning if any exception is triggered with computation
            logging.warning(f'{exception.__class__.__name__} exception was raise' +
                            f' while setting total_days for key {key}: {exception}')
        finally:
            # Set Unknown if any value couldn't be computed
            value['total_days'] = 'Unknown' if 'total_days' not in value else value['total_days']
            value['total_price'] = 'Unknown' if 'total_price' not in value else value['total_price']
            value['sqrt_total_price'] = 'Unknown' if 'sqrt_total_price' not in value \
                else value['sqrt_total_price']
            value['unit_cost'] = 'Unknown' if 'unit_cost' not in value else value['unit_cost']

        logging.info(f'Computed value for key {key}: {value}')

    return cal_data


def save_to_json(filename, data):
    """
    Saves the data into output file
    :param filename: output filename
    :param data: data which will be saved into file
    :return: none
    """
    if '.json' not in filename:
        filename = f'{filename}.json'
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as exception:
        logging.critical(f'Unable to write file {filename} due to:\n\t{exception}')
        exit(2)


def setup_logger(level=0):
    """
    Setup the logger for the program
    :param level: The log level for the program [ERROR, WARN, DEBUG, NONE (default)]
    :return: logger instance
    """
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    log_file_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'

    logger = logging.getLogger()
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logging_level = None
    if level == 3:
        logging_level = logging.CRITICAL
    elif level == 2:
        logging_level = logging.WARN
    elif level == 1:
        logging_level = logging.DEBUG
    if level == 0:
        logger.disabled = True
        return logger

    console_handler.setLevel(logging_level)
    file_handler.setLevel(logging_level)

    logger.setLevel(logging_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    """
    Main file for the program
    """
    # Start with Debug logger
    ARGS = parse_cmd_arguments()
    LOGGER = setup_logger(ARGS.debug)

    logging.debug('Starting the program ....')

    logging.debug(f'Loading the data from the input file {ARGS.input}')
    DATA = load_rentals_file(ARGS.input)
    logging.debug(f'File loaded')

    logging.debug(f'Loading the data from the input file {ARGS.input}')
    CAL_DATA = calculate_additional_fields(DATA)
    logging.debug(f'Additional fields calculated')

    logging.debug(f'Writing output file {ARGS.input}')
    save_to_json(ARGS.output, CAL_DATA)
    logging.debug(f'File saved to output file')

    logging.debug('Exiting the program ....')
    logging.shutdown()
