import csv
from pymongo import MongoClient

# need to run docker before this will work on this machine
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

import_data('assignment/data', 'product.csv', 'customers.csv', 'rental.csv')

