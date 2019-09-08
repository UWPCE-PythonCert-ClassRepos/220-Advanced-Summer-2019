"""
lesson 05
"""
import csv
from pymongo import MongoClient
from pprint import pprint
import time


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
    file_number = 0
    added = [0, 0, 0]
    errors = [0, 0, 0]
"""

    record_list = []
    for filepath in files:
        added = 0
        start_time = time.time()
        print(f"opening files: {filepath}")
        collection_name = filepath.split(".")[0]
        cursor = db[collection_name]
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
                        added += 1
                    except Exception as e:
                        print(e)
                        """errors[file_number] += 1
        file_number += 1"""
        record_list.append((added, 0, added, time.time() - start_time))
    return record_list


def show_available_products():
    """
    Query to return dictionary of:
    {product_id: {description, product_type, quantity_available}}
    Where quantity available is > 0
    """
    results = {}
    cursor = db["product"]
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
    results = {}
    rent_cursor = db["rental"]
    query = {"product_id": {"$eq": product_id}}
    users_renting = rent_cursor.find(query)
    for user in users_renting:
        user_cursor = db["customers"]
        query = {"user_id": {"$eq": user["user_id"]}}
        user_info = user_cursor.find(query)[0]
        results.update({user["user_id"]: {
                       "name": user_info["name"],
                       "address": user_info["address"],
                       "phone_number": user_info["phone_number"],
                       "email": user_info["email"]}})
    return results


if __name__ == "__main__":
    mongo = MongoClient("mongodb://127.0.0.1:27017")
    db = mongo["norton"]
    db["customers"].drop()
    db["rental"].drop()
    db["product"].drop()
    pprint(import_data("../data", "customers.csv",
                                  "product.csv"))
    """
    print(f"Successfully added {added} for customers, rentals and products")
    print(f"Failed to added {errors} for customers, rentals and products")
    print("available_products")
    pprint(show_available_products())
    print("prd0001")
    pprint(show_rentals("prd0001"))
    print("prd0002")
    pprint(show_rentals("prd0002"))
    print("prd0005")
    pprint(show_rentals("prd0005"))
    """
    mongo.close
