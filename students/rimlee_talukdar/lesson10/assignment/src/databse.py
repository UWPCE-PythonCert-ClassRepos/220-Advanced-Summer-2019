import csv
import datetime
import os.path
from pymongo import MongoClient
from types import FunctionType
from functools import wraps


def log_time(method):
        @wraps(method)
        def wrapped(*args, **kwrds):
            with open('data/timings.txt', 'a+') as timings:
                start = datetime.datetime.now()
                ret = method(*args, **kwrds)
                timings.write(str(method.__qualname__) + ":" + str((datetime.datetime.now() - start).total_seconds()) + "\n")
                return ret
        return wrapped


class TimerMetaClass(type):

    def __new__(meta, classname, bases, classDict):
        newClassDict = {}
        for attributeName, attribute in classDict.items():
            if isinstance(attribute, FunctionType):
                # replace it with a wrapped version
                attribute = log_time(attribute)
            newClassDict[attributeName] = attribute

        return type.__new__(meta, classname, bases, newClassDict)


class FurnitureDatabase(object, metaclass=TimerMetaClass):

    def __init__(self):

        mongo = MongoClient('localhost:32768')

        self.db = mongo['hp_norton']
        self.db.drop_collection('products')
        self.db.drop_collection('customers')
        self.db.drop_collection('rentals')

    def import_data(self, data_dir, *files):
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
                            cursor = self.db[collection_name]
                            cursor.insert_one(data)
                            added[file_number] += 1
                    except Exception:
                        errors[file_number] += 1
                file_number += 1
        return tuple(added), tuple(errors)


    def show_available_products(self):
        '''
            Return the available product catalog
            :returns dict of product id as key and
                        product description, product_type and quantity_available as value
        '''
        available_products = {}
        for product in iter(self.db['products'].find({'quantity_available': {'$gt': '0'}})):
            available_products.update({product['product_id']: {
                'description': product['description'],
                'product_type': product['product_type'],
                'quantity_available': product['quantity_available']
            }})
        return available_products


    def show_rentals(self, product_id):
        """

        """
        rental_information = {}

        # List of customers renting the product
        customers = [rental['user_id'] for rental in iter(self.db['rentals'].find({'product_id': {'$eq': product_id}}))]
        for user in self.db['customers'].find({'user_id': {'$in': customers}}):
            rental_information.update({user['user_id']: {
                    'name': user['name'],
                    'address': user['address'],
                    'phone_number': user['phone_number'],
                    'email': user['email']
                }})
        return rental_information

if __name__ == '__main__':
    db = FurnitureDatabase()
    db.import_data('data/', 'customer.csv')
    db.import_data('data/', 'product.csv')
    db.import_data('data/', 'rental.csv')

    print(db.show_available_products())
    print(db.show_rentals('P000006'))
