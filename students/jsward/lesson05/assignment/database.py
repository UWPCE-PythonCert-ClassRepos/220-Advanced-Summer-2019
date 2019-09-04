# They are not, in fact, constants...
# pylint: disable=C0103

# pylint: disable=W0703
"""
Assignment 5
database.py

Relational concept  Mongo DB equivalent
Database	        Database
Tables	            Collections
Rows	            Documents
Index	            Index
"""

import csv
import datetime
import logging
import sys

from pymongo import MongoClient
from pymongo import errors as pymongo_errors

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("mongo_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

mongo_client = MongoClient("mongodb://localhost:27017")
assignment_db = mongo_client["assignment"]


def import_data(data_dir, *files):
    """ Imports data from file(s) to mongodb"""
    record_counts = []
    error_counts = []
    for file_path in files:
        record_count = 0
        error_count = 0
        collection_name = file_path.split(".")[0]
        with open("/".join([data_dir, file_path])) as file:
            reader = csv.reader(file, delimiter=",")
            header = False
            for row in reader:
                if not header:
                    header = [h.strip("\ufeff") for h in row]
                else:
                    data = {header[i]:v for i, v in enumerate(row)}
                    cursor = assignment_db[collection_name]
                    try:
                        cursor.insert_one(data)
                        record_count += 1
                        logger.debug("Inserted record %s into collection %s", data, collection_name)
                    except pymongo_errors.ServerSelectionTimeoutError as ex:
                        logger.error("Timeout or connection refused when connecting to MongoDB: %s", ex)
                        error_count += 1
                        break
                    except Exception as ex:
                        logger.error("Error inserting record %s into table %s in MongoDB %s Error: %s",
                                     data, assignment_db.name, mongo_client, ex)
                        error_count += 1
                        continue
        record_counts.append(record_count)
        error_counts.append(error_count)
        logger.info("Inserted %s records into collection %s", record_count, collection_name)
        logger.info("Encountered %s errors while inserting records into collection %s", error_count, collection_name)
    return tuple(record_counts), tuple(error_counts)


def show_available_products(products_collection='products'):
    """
    Lists available products
    :return:
    A python dictionary of products listed as available with the following fields:
    * product_id.
    * description.
    * product_type.
    * quantity_available.

    {‘prd001’:{‘description’:‘60-inch TV stand’,’product_type’:’livingroom’,’quantity_available’:‘3’},
    ’prd002’:{‘description’:’L-shaped sofa’,’product_type’:’livingroom’,’quantity_available’:‘1’}}
    """
    available_products = {}
    cursor = assignment_db[products_collection]
    try:
        for product in cursor.find():  # {"quantity_available": {"$gte": 1}}):
            if int(product['quantity_available']) >= 1:
                available_products[product['product_id']] = {'description': product['description'],
                                                             'product_type': product['product_type'],
                                                             'quantity_available': product['quantity_available']}
    except pymongo_errors.ServerSelectionTimeoutError as ex:
        logger.error("Timeout or connection refused when connecting to MongoDB: %s", ex)
    except Exception as ex:
        logger.error("Error retrieving available products from collection %s: %s", products_collection, ex)
    logger.debug("Retrieved %s available products from %s", len(available_products), products_collection)
    return available_products


def show_rentals(product_id, rentals_collection='rentals', customers_collection='customers'):
    """
    Lists customers who have rented a product
    :return:
    A Python dictionary with the following user information from users that have rented products matching product_id:
    * user_id.
    * name.
    * address.
    * phone_number.
    * email.

    {‘user001’:{‘name’:’Elisa Miles’,’address’:‘4490 Union Street’,’phone_number’:‘206-922-0882’,
    ’email’:’elisa.miles@yahoo.com’},’user002’:{‘name’:’Maya Data’,’address’:‘4936 Elliot Avenue’,
    ’phone_number’:‘206-777-1927’,’email’:’mdata@uw.edu’}}
    """
    user_ids = []
    rentals_cursor = assignment_db[rentals_collection]
    try:
        for rental in rentals_cursor.find({"product_id": product_id}):
            if rental['user_id'] not in user_ids:
                user_ids.append(rental['user_id'])
    except Exception as ex:
        logger.error("Error retrieving rentals of product_id %s from %s: %s", product_id, rentals_collection, ex)
        return {}
    logger.debug("%s users rented %s", len(user_ids), product_id)
    renters = {}
    customers_cursor = assignment_db[customers_collection]
    for user_id in user_ids:
        try:
            record = customers_cursor.find_one({"user_id": user_id})
            if record:
                renters[record['user_id']] = {'name': record['name'], 'address': record['address'],
                                              'phone_number': record['phone_number'], 'email': record['email']}
        except Exception as ex:
            logger.error("Error finding user_id %s in %s: %s", user_id, customers_collection, ex)
            continue
    logger.debug("The following customers rented product_id %s: %s", product_id, renters)
    return renters


if __name__ == "__main__":
    # logger.info("Script started at %s", datetime.datetime.now())
    # # results = import_data('data', 'customers.csv', 'products.csv', 'rentals.csv')
    # # logger.info("Stats: %s", results)
    # a_p = show_available_products()
    # results = show_rentals('prd002')
    # print(results)
    # logger.info("Script ended at %s", datetime.datetime.now())
    pass
