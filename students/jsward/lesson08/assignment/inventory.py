# pylint: disable=C0103
# pylint: disable=W0703

"""
inventory.py
CSV replacement
"""

import datetime
import functools
import logging
import sys

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("inventory_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def add_furniture(invoice_file, customer_name, item_code, item_description, item_monthly_price):
    """ Creates invoice_file if it doesn't exist or append if it does.  Adds item record to file."""
    try:
        with open(file=invoice_file, mode='a') as file:
            record = "{}, {}, {}, {}\n".format(customer_name, item_code, item_description, item_monthly_price)
            file.write(record)
            logger.debug("Wrote line %s to %s", record, invoice_file)
    except OSError as er:
        logger.error("Failed to open %s.  The error was: %s", invoice_file, er)


def single_customer(customer_name, invoice_file):
    """
    Uses closure to return a function that will iterate through rental_items and add each
    item to invoice_file

    :return: returns a function that takes one parameter, rental_items
    """
    def return_function(rental_items):
        """ Creates invoice_file if it doesn't exist or append if it does.  Adds item record to file."""
        try:
            with open(file=invoice_file, mode='a') as file:
                for item in rental_items:
                    item = item.strip('\n')
                    record = "{},{}\n".format(customer_name, item)
                    file.write(record)
                    logger.debug("Wrote line %s to %s", record, invoice_file)
        except OSError as er:
            logger.error("Failed to open %s.  The error was: %s", invoice_file, er)
    return return_function


if __name__ == '__main__':
    add_furniture('invoices.csv', 'first last', 'LR04', 'Leather sofa', 25.00)
    add_furniture('invoices.csv', 'Edward Data', 'KT78', 'Kitchen Table', 10.00)

    with open('data/test_items.csv', 'r') as test_items:
        rentals = test_items.readlines()
    # single_customer works, but doesn't use functools.partial
    single_customer('A A', 'invoices.csv')(rentals)

    # Using functools.partial outside the function works too, but is less efficient.
    # I'm sure this isn't what the author had in mind.
    functools.partial(single_customer, customer_name='G G', invoice_file='invoices.csv')()(rentals)

    # I can see above that I've duplicated much of the code in add_furniture to create single_customer.
    # I assume I was supposed to use functools.partial to re-use the add_furniture function inside
    # single_customer, but I don't see a way to do that while still adhering to the input and output requirements
    # specified for each function in the assignment.
