"""
lesson 05
"""
import csv
from pymongo import MongoClient
from pprint import pprint


class MongoDBConnection:
    def __init__(self, host="localhost", port="27017"):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None
        self.db = None
        self.product = None
        self.customers = None
        self.rental = None

    def __enter__(self):
        self.connection = MongoClient(self.host)
        self.db = self.connection.media
        self.product = self.db["product"]
        self.customers = self.db["customers"]
        self.rental = self.db["rental"]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def import_data(directory_name, *files):
    """
    import_data(directory_name, product_file, customer_file, rentals_file):
    This function takes a directory name three csv files as input,
    one with product data, one with customer data and
    the third one with rentals data and creates and populates
    a new MongoDB database with these data.
    It returns 2 tuples:
    the first with a record count of the number of products,
    customers and rentals added (in that order),
    the second with a count of any errors that occurred, in the same order
"""
    with mongo:
        file_number = 0
        added = [0, 0, 0]
        errors = [0, 0, 0]
        for filepath in files:
            print(f"opening files: {filepath}")
            collection_name = filepath.split(".")[0]
            cursor = mongo.db[collection_name]
            with open("/".join([directory_name, filepath])) as file:
                reader = csv.reader(file, delimiter=",")
                header = []
                for row in reader:
                    if not header:
                        # not using strip(\ufeff) as got different error
                        header = [h.strip("ï»¿") for h in row]
                    else:
                        data = {header[i]: val for i, val in enumerate(row)}
                        try:
                            cursor.insert_one(data)
                            added[file_number] += 1
                        except Exception as e:
                            print(e)
                            errors[file_number] += 1
            file_number += 1
        return tuple(added), tuple(errors)


def show_available_products():
    """
    Query to return dictionary of:
    {product_id: {description, product_type, quantity_available}}
    Where quantity available is > 0
    """
    with mongo:
        results = {}
        cursor = mongo.db["product"]
        query = {"quantity_available": {"$gt": "0"}}
        available_products = cursor.find(query)
        for product in available_products:
            results.update({product['product_id']: {
                           'description': product['description'],
                           'product_type': product['product_type'],
                           'quantity_available': product['product_type']}})
        return results


def show_rentals(product_id):
    """
    Query to return dictionary of customer info
    Where customer has rented product
    """
    with mongo:
        results = {}
        rent_cursor = mongo.db["rental"]
        query = {"product_id": {"$eq": product_id}}
        users_renting = rent_cursor.find(query)
        for user in users_renting:
            user_cursor = mongo.db["customers"]
            query = {"user_id": {"$eq": user["user_id"]}}
            user_info = user_cursor.find(query)[0]
            results.update({user["user_id"]: {
                           "name": user_info["name"],
                           "address": user_info["address"],
                           "phone_number": user_info["phone_number"],
                           "email": user_info["email"]}})
        return results


def drop_data():
    with mongo:
        mongo.db["customers"].drop()
        mongo.db["rental"].drop()
        mongo.db["product"].drop()


if __name__ == "__main__":
    global mongo
    mongo = MongoDBConnection()
    [added, errors] = import_data("../data",
                                  "customers.csv",
                                  "rental.csv",
                                  "product.csv")
    print(f"Successfully added {added} for customers, rentals and products")
    print(f"Failed to added {errors} for customers, rentals and products")
    print("available_products")
    pprint(show_available_products())
    print("prd001")
    pprint(show_rentals("prd001"))
    print("prd002")
    pprint(show_rentals("prd002"))
    print("prd005")
    pprint(show_rentals("prd005"))
    drop_data()
