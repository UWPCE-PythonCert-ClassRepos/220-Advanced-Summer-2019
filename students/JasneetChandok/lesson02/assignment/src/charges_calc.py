'''
Returns total price paid for individual rentals 
'''
import argparse
import json
import datetime
import math
import logging


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d', '--debug', help='set logging level (1-4)', required=False, default=1)

    return parser.parse_args()


def setup_logging(level='1'):
    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()

    if level == '2':
        file_handler.setLevel(logging.ERROR)
        console_handler.setLevel(logging.ERROR)
        logger.setLevel(logging.ERROR)
    elif level == '3':
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.WARNING)
        logger.setLevel(logging.WARNING)
    elif level == '4':
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:  
        file_handler.setLevel(logging.CRITICAL)
        console_handler.setLevel(logging.CRITICAL)
        logger.setLevel(logging.CRITICAL)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
            logger.debug(f'Successfully loaded {len(data.keys())} elements from {filename}')
        except Exception as e:
            logger.error(f'Could not import date from {filename}: {e}')
            exit(0)
    return data


def calculate_additional_fields(data):
    for value in data.values():
        if value['rental_start'] > value['rental_end']:
            logger.error('start date before end date. Skipping...')
        else:
            try:
                rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
                logger.debug(f'calculated rental_start: {rental_start}')
                rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
                logger.debug(f'calculated rental_end: {rental_end}')
                value['total_days'] = (rental_end - rental_start).days
                logger.debug(f'calculated total_days: {value["total_days"]}')
                value['total_price'] = value['total_days'] * value['price_per_day']
                logger.debug(f'calculated total_price: {value["total_price"]}')
                value['sqrt_total_price'] = math.sqrt(value['total_price'])
                logger.debug(f'calculated sqrt_total_price: {value["sqrt_total_price"]}')
                value['unit_cost'] = value['total_price'] / value['units_rented']
                logger.debug(f'calculated unit_cost: {value["unit_cost"]}')
            except Exception as e:
                logger.error(f'Could not calculate additional fields: {e}')
    return data

    return data


def save_to_json(filename, data):
    logging.debug(f'writing data to {filename}')
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f'could not write data to {filename}: {e}')


if __name__ == "__main__":
    args = parse_cmd_arguments()
    logger = setup_logging(level=args.debug)
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
