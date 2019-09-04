""" Inheriting Lesson 05 Mongo """

import csv
import threading
from pprint import pprint
from pymongo import MongoClient

mongo = MongoClient('mongodb://localhost:27017')
db = mongo['norton']

def import_data(data_dir, *files):
    for file_path in files:
        print(f'opening file: {file_path}')
        collection_name = file_path.split('.')[0]
        print(f'creating collection: {collection_name}')

        with open('/'.join([data_dir, file_path])) as file:
            reader = csv.reader(file, delimiter=',')

            header = False
            table = db[collection_name]

            for row in reader:
                if not header:
                    header = [h for h in row]
                else:
                    data = {header[i]:v for i,v in enumerate(row)}
                    print(data)
                try:
                    table.insert_one(data)
                except Exception as e:
                    print(e)


def import_data_multithreaded(file_path):
    print(f'opening file: {file_path}')
    collection_name = file_path.split('.')[0]
    print(f'creating collection: {collection_name}')

    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')

        header = False
        table = db[collection_name]

        for row in reader:
            if not header:
                header = [h for h in row]
            else:
                data = {header[i]:v for i,v in enumerate(row)}
                print(data)
            try:
                table.insert_one(data)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    db["customer"].drop()
    db["product"].drop()
    db["rental"].drop()
    # import_data('data', 'customer.csv', 'product.csv', 'rental.csv')

    files = [
        'data/product.csv',
        'data/rental.csv',
        'data/customer.csv',
    ]

    threads = []

    for file_path in files:
        thread = threading.Thread(target=import_data_multithreaded, args=(file_path,))
        thread.start()
        threads.append(thread)
