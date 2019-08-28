"""
As a HP Norton customer I want to see a list of all products available for rent so that I can make a rental choice.

As a HP Norton salesperson I want to see a list of all of the different products, showing product ID, description, product type and quantity available.

As a HP Norton salesperson I want to see a list of the names and contact details (address, phone number and email) of all customers who have rented a certain product.
"""

from pymongo import MongoClient
import csv

client = MongoClient(port=27017)
db = client.admin


def import_data():
    with open('customers.csv', newline="") as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                
        print(f'Processed {line_count} lines.')

def show_available_products():
    pass

def list_unique_products():
    pass

def show_rentals():
    pass
