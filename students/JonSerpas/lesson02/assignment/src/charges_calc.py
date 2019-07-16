'''
Returns total price paid for individual rentals 
'''
import argparse
import json
import datetime
import math
import logging

# defining the format for logs as they are written to the logfile
log_format = '%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s'
formatter = logging.Formatter(log_format)

log_file = datetime.datetime.now().strftime('%Y-%m-%d')+".log"
file_handler = logging.FileHandler(log_file)


file_handler.setFormatter(formatter)

logger = logging.getLogger()

logger.addHandler(file_handler)
# sets the format style for log file output
# log_file = datetime.datetime.now().strftime(“%Y-%m-%d”)+’.log’


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input',
                        help='input JSON file',
                        required=True,)
    parser.add_argument('-o', '--output',
                        help='ouput JSON file',
                        required=True)
    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename, 'r') as file:
        loaded_json_data = json.load(file)
        # try:
        #     data = json.load(file)
        # except:
        #   # exit(0)
        # this oddly doesn't work with try / except because magic???
    return loaded_json_data


def calculate_additional_fields(data):
    output = []
    for key, value in data.items():
        try:  # validating non '' data
            if value['rental_start'] and value['rental_end']:
                rental_start = datetime.datetime.strptime(
                    value['rental_start'], '%m/%d/%y')
                rental_end = datetime.datetime.strptime(
                    value['rental_end'], '%m/%d/%y')
                value['total_days'] = (rental_end - rental_start).days

                # some dates appear to be off and giving a neg int
                # abs() allows the stop start to always be pos int
                value['total_price'] = abs(
                    value['total_days']) * value['price_per_day']
                value['sqrt_total_price'] = math.sqrt(
                    value['total_price'])
                value['unit_cost'] = \
                    value['total_price'] / value['units_rented']
                value['key'] = key
                output.append(value)
            else:
                print(value)
        except ZeroDivisionError as zero_error:
            logging.warning(zero_error)
            pass
        except Exception as some_error:
            logging.error(some_error)
            # exit(0)
        # wouldn't we want to return the above variables?
        # this looks to be returning the exact same data.
    return output


def save_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    data = load_rentals_file(args.input)
    parsed_json_data = calculate_additional_fields(data)
    save_to_json(args.output, parsed_json_data)
    # save_to_json(args.output, data)
