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

    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        output = json.load(file)

    return output


def calculate_additional_fields(input):
    for key, value in input.items():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
        except ValueError:
            rental_start = datetime.datetime(2019, 12, 31)
            logging.warning(
                "Invalid rental start time, default to 2019/12/31, key: %s, product_code: %s, rental_start: %s",
                key,
                value["product_code"],
                rental_start)
        try:
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
        except ValueError:
            rental_end = datetime.datetime(2019, 12, 31)
            logging.warning("Invalid rental end time, default to 2019/12/31")

        if rental_start > rental_end:
            value['total_days'] = 0
            logging.warning(
                "Rental start time cannot be after the end time, key: %s, "
                "product_code: %s, rental_start: %s, renal_end: %s",
                key,
                value["product_code"],
                rental_start,
                rental_end)
        else:
            value['total_days'] = (rental_end - rental_start).days

        value['total_price'] = value['total_days'] * value['price_per_day']
        value['sqrt_total_price'] = math.sqrt(value['total_price'])
        try:
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except ZeroDivisionError:
            value['unit_cost'] = 0
            logging.warning("Units rented cannot be 0, default unit cost to 0")

    return data


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
