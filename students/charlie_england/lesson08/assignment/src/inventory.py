
import csv

def create_csv_writer(invoice_file):
    """
        takes an invoice file to write to and returns a function that when called with
        customer, item_code, item_description, and item_quantity will write these items
        to the invoice that it was created with
    """
    def add_transaction(customer, item_code, item_description, item_quantity):
        with open(invoice_file,"a") as file:
            writer = csv.writer(file)
            writer.writerow([customer,item_code,item_description,item_quantity])
    return add_transaction

def single_customer(customer_name, invoice_file):
    """
        takes a customer name and an invoice and returns a function that will write
        to this invoice file, when sent a file of rental items, will open this file and
        write to the invoice file with the customer name and all the items
    """
    def add_rental_items(rental_items):
        items_list = []
        with open(rental_items,'r') as file:
            [items_list.append(line.strip('\r\n').split(',')) for line in file.readlines()]
        with open(invoice_file,'a') as file:
            writer = csv.writer(file)
            [writer.writerow([customer_name,*item_info]) for item_info in items_list]
    return add_rental_items