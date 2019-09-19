import csv
from functools import partial


def add_furniture(invoice_file, customer_name, item_code,
                  item_description, item_monthly_price):
    '''
    This function adds customer invoice to a file. It will create the file if it does not exit
    else append it
    :param invoice_file: spreadsheat data where customer data will exist
    :param customer_name: customer name
    :param item_code: item code of the product
    :param item_description: items discription
    :param item_monthly_price: monthly price of the item
    :return: none
    '''
    with open(invoice_file, mode='a+') as invoice:
        writer = csv.writer(invoice, delimiter=',')
        writer.writerow([customer_name, item_code, item_description, item_monthly_price])


def single_customer(customer_name, invoice_file):
    '''
    This function create a function that will read the invoice data from a file,
    and copies the content to another file while changing the name of the customer
    :param customer_name: New customer name
    :param invoice_file: spreadsheet data file
    :return: function that will create the file for the indivisual customer
    '''
    def create_invoice(rental_items):
        '''
        This function will copy the content from a invoice data file and
        copies the content to rental file while changing the name of the customer
        :param rental_items: the file name for the customer
        :return: none
        '''
        add_rental_furniture = partial(add_furniture, rental_items)

        with open(invoice_file, mode='r') as invoice:
            reader = csv.reader(invoice, delimiter=',')

            for row in reader:
                row[0] = customer_name
                add_rental_furniture(*row)

    return create_invoice
