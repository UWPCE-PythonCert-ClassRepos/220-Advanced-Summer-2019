""""
download mongodb
create the following directories for your project
data
data/db
must use 127.0.0.1 on windows
pip install pymongo
"""
import logging
from os.path import join, abspath
from pymongo import MongoClient
from pymongo import errors
import pandas as pd
# noqa # pylint: disable=too-few-public-methods, too-many-locals

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class MongoDBConnection(object):
    """MongoDB Connection"""
    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def print_collection(collection_name):
    '''
    function to print a given table (collection_name)
    '''
    for doc in collection_name.find():
        print(doc)


def delete_database():
    '''
    function to delete all tables
    '''

    mongo = MongoDBConnection()

    with mongo:
        db_hp = mongo.connection.HPNorton
        customers = db_hp["customers"]
        inventory = db_hp["inventory"]
        rental = db_hp["rental"]

        customers.drop()
        inventory.drop()
        rental.drop()


def import_data(directory_name, product_file, customer_file, rental_file):

    """function to imports data from csv files and puts in database"""
    mongo = MongoDBConnection()

    inventory_error, customer_error, rental_error = 0, 0, 0
    inventory_count, customer_count, rental_count = 0, 0, 0

    with mongo:
        # mongodb database; it all starts here
        db_hp = mongo.connection.HPNorton

        # collection in database
        customers = db_hp["customers"]
        inventory = db_hp["inventory"]
        rental = db_hp["rental"]

        # notice how easy these are to create and that they are "schemaless"
        # that is, the Python module defines the data structure in a dict,
        # rather than the database which just stores what it is told

        try:
            inventory_df = pd.read_csv(join(abspath(directory_name), product_file))
            inventory_input = inventory_df.to_dict('records')
            inventory.insert_many(inventory_input)
            inventory_count = inventory_df.shape[0]

        except (FileNotFoundError, errors.PyMongoError) as exc:
            inventory_error += 1
            LOGGER.error(f"Can not load {product_file} file.  Exception {exc}")

        try:
            customers_df = pd.read_csv(join(abspath(directory_name), customer_file))
            customers_input = customers_df.to_dict('records')
            customers.insert_many(customers_input)
            customer_count = customers_df.shape[0]

        except (FileNotFoundError, errors.PyMongoError) as exc:
            customer_error += 1
            LOGGER.error(f"Can not load {customer_file} file.  Exception {exc}")

        try:
            rental_df = pd.read_csv(join(abspath(directory_name),
                                         rental_file))
            rental_input = rental_df.to_dict('records')
            rental.insert_many(rental_input)
            rental_count = rental_df.shape[0]

        except (FileNotFoundError, errors.PyMongoError) as exc:
            rental_error += 1
            LOGGER.error(f"Can not load {rental_file} file.  Exception {exc}")

        error_count = (inventory_error, customer_error, rental_error)
        record_count = (inventory_count, customer_count, rental_count)

        return (record_count, error_count)


def show_rentals(product_id):
    '''
    function to show all users for a given product_id
    '''
    # related data
    mongo = MongoDBConnection()

    with mongo:
        db_hp = mongo.connection.HPNorton
        result = []
        rental = db_hp['rental']
        customers = db_hp['customers']

        for product in rental.find({'Product_ID':product_id}):
            query = {"Customer_ID": product["Customer_ID"]}
            for a_customer in customers.find(query):
                a_customer.pop("Credit_Limit", None)
                a_customer.pop("Status", None)
                a_customer.pop("_id", None)
                result.append(a_customer)
    return result


def show_customers():
    '''
    function to show all customers
    '''
    results = {}
    mongo = MongoDBConnection()
    with mongo:
        # mongodb database; it all starts here
        db_hp = mongo.connection.HPNorton
        customers = db_hp['customers']
        for a_customer in customers.find():
            a_customer.pop("_id", None)
            results[a_customer['Customer_ID']] = a_customer

    return results


def show_available_products():
    '''
    function to show all available products
    '''
    results = {}
    mongo = MongoDBConnection()
    with mongo:
        # mongodb database; it all starts here
        db_hp = mongo.connection.HPNorton
        inventory = db_hp["inventory"]
        for a_product in inventory.find():
            a_product.pop("_id", None)
            results[a_product['Product_ID']] = a_product
