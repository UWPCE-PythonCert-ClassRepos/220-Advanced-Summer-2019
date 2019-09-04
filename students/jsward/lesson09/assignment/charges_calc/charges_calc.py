# pylint: disable=C0103
"""
charges_calc.py

This script intentionally implements logging in a different manner than the assignment specifies.
* Script uses DEBUG, INFO, WARN and ERROR logging levels.
* The logging level can be set by the person running the script via the -ll argument, and defaults to INFO
* Logging to file is off by default, and can be enabled with the -ltf flag
"""

import argparse
import json
import datetime
import math
import logging
import sys


log_format = "%(asctime)s\t%(filename)s\t:%(lineno)-3d\t%(levelname)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("charge_calc_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel('INFO')
logger.addHandler(stream_handler)


def conditional_logging(original_function):
    """Decorator that will disable logging if the --dl flag is set when the script is run"""
    def wrapper(*args, **kwargs):
        if cmd_args.disable_some_logging:
            previous_logging_level = logger.getEffectiveLevel()
            logger.setLevel("CRITICAL")
            original_function(*args, **kwargs)
            logger.setLevel(previous_logging_level)
        else:
            original_function(*args, **kwargs)
    return wrapper


def parse_cmd_arguments():
    """Processes arguments passed to script via the command line"""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='Path of input JSON file.', required=True)
    parser.add_argument('-o', '--output', help='Path of output JSON file.', required=True)
    parser.add_argument('-ll', '--log_level', help='Set logging level.  Defaults to INFO.', required=False,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO')
    parser.add_argument('-ltf', '--log_to_file', action='store_true', required=False)
    parser.add_argument('-dl', '--disable_some_logging', action='store_true', required=False)

    logger.debug("Arguments passed to script: %s", parser.parse_args())
    return parser.parse_args()


def load_rentals_file(filename):
    """Loads JSON data from file"""
    logger.debug("Entering load_rentals_file function")
    try:
        with open(filename) as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                # Original except was generic, and silently exited on error.  No good!
                logger.error("Error loading JSON data from %s: %s.  Exiting script...", filename, e)
                sys.exit(1)
    except FileNotFoundError as e:
        logger.error("Error opening %s: %s.  Exiting script...", filename, e)
        sys.exit(1)
    logger.info("Loaded %s records from %s", len(data), filename)
    return data


@conditional_logging
def calculate_additional_fields(data):
    """Calculates additional values based on input JSON data"""
    logger.debug("Entering calculate_additional_fields function")
    records_calculated = 0
    for value in data.values():
        # Original try/except includes too many operations

        try:
            # Rental start and end fields are backwards in the source data, brilliant.
            date1 = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
        except ValueError:
            logger.error("Product Code %s has an invalid rental_start date of %s", value['product_code'],
                         value['rental_start'])
            continue

        try:
            # Rental start and end fields are backwards in the source data, brilliant.
            date2 = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
        except ValueError:
            logger.error("Product Code %s has an invalid rental_end date of %s", value['product_code'],
                         value['rental_end'])
            continue

        # Since rental dates are mixed up, will set the earlier date to rental_start and the later date to rental_end
        if date2 < date1:
            rental_start = date2
            rental_end = date1
            logger.debug("For Product Code %s rental_start is %s, rental_end is %s", value['product_code'],
                         rental_start, rental_end)
        else:
            rental_start = date1
            rental_end = date2
            logger.debug("For Product Code %s rental_start is %s, rental_end is %s", value['product_code'],
                         rental_start, rental_end)

        try:
            value['total_days'] = (rental_end - rental_start).days
        except ValueError as e:
            logger.warning("error calculating total_days for Product Code %s: %s", value['product_code'], e)
            value['total_days'] = 0

        if value['total_days'] < 0:
            logger.warning("Invalid total_days of %s for Product Code %s.  Total_days will be set to 0",
                           value['total_days'], value['product_code'])
            value['total_days'] = 0

        try:
            value['total_price'] = value['total_days'] * value['price_per_day']
        except ValueError as e:
            logger.warning("error calculating total_price for Product Code %s: %s", value['product_code'], e)
            value['total_price'] = 0

        try:
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
        except ValueError as e:
            logger.warning("Failed to calculate sqrt_total_price for Product Code %s.  Error: %s",
                           value['product_code'], e)
            value['sqrt_total_price'] = 0

        if value['units_rented'] > 0:
            value['unit_cost'] = value['total_price'] / value['units_rented']
        else:
            # Original except was generic, and silently exited on error.  No good!
            logger.warning("Error calculating unit_cost for Product Code %s: %s units rented", value['product_code'],
                           value['units_rented'])
            value['unit_cost'] = 0
        records_calculated += 1
    logger.info("Calculated fields for %s records", records_calculated)
    logger.debug("data with calculated fields:\n%s", data)
    return data


def save_to_json(filename, data):
    """Saves JSON data to file"""
    logger.debug("Entering save_to_json function")
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
            logger.info("JSON data written to %s", filename)
    except FileNotFoundError as e:
        logger.error("Error writing JSON data to %s: %s.  Exiting script...", filename, e)
        sys.exit(1)


if __name__ == "__main__":
    cmd_args = parse_cmd_arguments()
    if cmd_args.log_to_file:
        logger.addHandler(file_handler)
    logger.info("Script started at %s", datetime.datetime.now())
    logger.info("Setting logging level to %s", cmd_args.log_level)
    logger.setLevel(cmd_args.log_level)

    loaded_data = load_rentals_file(cmd_args.input)

    calculated_data = calculate_additional_fields(loaded_data)

    save_to_json(cmd_args.output, calculated_data)

    logger.info("Script ended at %s", datetime.datetime.now())
