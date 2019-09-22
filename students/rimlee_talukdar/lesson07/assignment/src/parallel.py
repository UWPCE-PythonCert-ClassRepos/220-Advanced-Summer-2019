import csv
import datetime
import os.path

from pymongo import MongoClient
from multiprocessing.pool import ThreadPool

mongo = MongoClient('localhost:32768')

db = mongo['hp_norton']
db.drop_collection('product')
db.drop_collection('customer')
db.drop_collection('rental')


def import_data(file_path, collection_name):
    """
    Load data given data directory and file name
    :param file_path: data file path
    :param collection_name: collection name where data will be stored
    :return: returns total number of records processed, initial number of records,
            final record stored and total time required to store the data
    """
    start_time = datetime.datetime.now()
    initial_record_count = db[collection_name].count()
    records_processed = 0
    pool = ThreadPool(10)

    data = []
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        header = False

        for row in reader:
            if not header:
                header = [h.strip('\ufeff') for h in row]
            else:
                data.append((collection_name,
                             {key: value.strip('\ufeff') for key, value in zip(header, row)}))

    save_status = pool.map_async(save_item, data).get()

    for item_status in save_status:
        records_processed += 1 if item_status else 0

    final_record_count = db[collection_name].count()

    return records_processed, \
           initial_record_count, \
           final_record_count, \
           (datetime.datetime.now() - start_time).total_seconds()


def save_item(args):
    """
    Save an item in the collection
    :param collection_name: name of the collection
    :param data: data to be stored
    :return: True if data been stored else return false.
    """
    collection_name = args[0]
    data = args[1]
    try:
        cursor = db[collection_name]
        cursor.insert_one(data)
        return True
    except Exception:
        return False


def parallel():
    """
        Store data in parallel pattern
        :return: returns total number of records processed, initial number of records,
                final record stored and total time required to store the data
        """
    result = []
    for filepath in ['customer.csv', 'product.csv']:
        collection_name = filepath.split('.')[0]
        result.append(import_data(os.path.join('data/', filepath), collection_name))

    return result
