"""
As a HP Norton customer I want to see a list of all products available for rent so that I can make a rental choice.

As a HP Norton salesperson I want to see a list of all of the different products, showing product ID, description, product type and quantity available.

As a HP Norton salesperson I want to see a list of the names and contact details (address, phone number and email) of all customers who have rented a certain product.
"""

from pymongo import MongoClient
from pprint import pprint

import csv

client = MongoClient('mongodb://localhost:27017')
db = client["norton"]
# db = client.admin


def import_data(data_dir, files):
    for filepath in files:
        print("Opening file %s" %filepath)
        collection_name = filepath.split('.')[0]
        print("Creating collection %s" %collection_name)
        with open('/'.join([data_dir, filepath]), encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file, delimiter=',')
            header = False
            for row in csv_reader:
                if not header:
                    header = [h for h in row]
                else:
                    data = {
                        header[i]:v
                        for i,v in enumerate(row)
                    }
                    table = db['norton']
                    try:
                        table.insert_one(data)
                    except Exception as e:
                        print(e)
                    pprint(data)

def show_available_products():
    pass

def list_unique_products():
    pass

def show_rentals():
    pass

if __name__ == "__main__":
    db["customer"].drop()
    db["product"].drop()
    db["rental"].drop()

    files = [
        "customers.csv",
        "product.csv",
        "rental.csv",
    ]
    import_data('data', files)
    print('Done!')