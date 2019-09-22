import csv
import os.path
from pymongo import MongoClient

mongo = MongoClient('localhost:32768')

db = mongo['hp_norton']
db.drop_collection('products')
db.drop_collection('customers')
db.drop_collection('rentals')

def import_data(data_dir, *files):
    """
        Load data given data directory and file name
    """
    added = [0, 0, 0]
    errors = [0, 0, 0]
    file_number = 0
    for filepath in files:
        collection_name = filepath.split('.')[0]
        with open(os.path.join(data_dir, filepath)) as file:
            reader = csv.reader(file, delimiter=',')
            header = False

            for row in reader:
                try:
                    if not header:
                        header = [h.strip('\ufeff') for h in row]
                    else:
                        data = {key: value.strip('\ufeff') for key, value in zip(header, row)}
                        cursor = db[collection_name]
                        cursor.insert_one(data)
                        added[file_number] += 1
                except Exception:
                    errors[file_number] += 1
            file_number += 1
    return tuple(added), tuple(errors)


def show_available_products():
    '''
        Return the available product catalog
        :returns dict of product id as key and
                    product description, product_type and quantity_available as value
    '''
    available_products = {}
    for product in iter(db['products'].find({'quantity_available': {'$gt': '0'}})):
        available_products.update({product['product_id']: {
            'description': product['description'],
            'product_type': product['product_type'],
            'quantity_available': product['quantity_available']
        }})
    return available_products


def show_rentals(product_id):
    """

    """
    rental_information = {}

    # List of customers renting the product
    customers = [rental['user_id'] for rental in iter(db['rentals'].find({'product_id': {'$eq': product_id}}))]
    for user in db['customers'].find({'user_id': {'$in': customers}}):
        rental_information.update({user['user_id']: {
                'name': user['name'],
                'address': user['address'],
                'phone_number': user['phone_number'],
                'email': user['email']
            }})
    return rental_information
