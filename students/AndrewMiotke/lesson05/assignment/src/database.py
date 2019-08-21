"""
Running this script:
    - Ensure docker is running mongod
    - Make sure mongo is running on port 27017
    - To run the docker container on port 27017
        docker run --name mongo -p 27017:27017 -d mongo mongod
"""

import csv
from pymongo import MongoClient

mongo = MongoClient("localhost:27017")
db = mongo['assignment']


def import_data(data_dir, *files):
    for filepath in files:
        collection_name = filepath.split('.')[0]

        with open('/'.join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=',')

            header = False
            for row in reader:
                if not header:
                    header = [h.strip('\ufeff') for h in row ]
                else:
                    data = {header[i]:v for i, v in enumerate(row)}
                    cursor = db[collection_name]
                    cursor.insert_one(data)

import_data('data/', 'product.csv', 'customers.csv', 'rental.csv')


def show_available_products():
    column = db['product']
    query = {'quantity_available':{'$gt':'0'}}
    results = {}
    available_products = iter(column.find(query))

    for product in available_products:
        product_id = product['product_id']
        description = product['description']
        product_type = product['product_type']
        quantity_available = product['quantity_available']

        results.update({product_id: {'description': description, 'product_type': product_type, 'quantity_available': quantity_available}})

        return results


def show_rentals():
    rental_column = db['rental']
    customers_columns = db['customers']
    query = {'product_id': {'$eq': product_id}}
    users_with_rentals = rental_column.find(query)
    rental_results = {}

    for user in users_with_rentals:
        user_id = user['user_id']
        query = {'user_id': {'$eq': user_id}}
        user_info = customers_columns.find(query)[0]
        name = user_info['name']
        address = address['address']
        phone_number = user_info['phone_number']
        email = user_info['email']

        rental_results.update({user_id: {'name': name, 'address': address, 'phone_number': phone_number, 'email': email}})

        return rental_results
