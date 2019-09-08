import csv
from pprint import pprint
from pymongo import MongoClient

import os

from datetime import datetime

import threading

# https://stackoverflow.com/questions/35813854/how-to-join-multiple-collections-with-lookup-in-mongodb

"""
High Level Requirements
- Create a product database with attributes that reflect the contents of the csv file.
- Import all data in the csv files into your MongoDB implementation.
- Write queries to retrieve the product data.
- Write a query to integrate customer and product data.
Detail Tests
- a file called database.py
- includes functions like 
    import_data(directory_name, product_file, customer_file, rentals_file)
    It returns 2 tuples: the first with a record count of the number of
products, customers and rentals added (in that order), the second with a count of any errors that occurred, in the same order.
"""

mongo = MongoClient("mongodb://localhost:27017")
db = mongo["norton"]


def import_data(data_dir, *files):

    customer_count = [0]*4
    product_count = [0]*4

    # get a prior count of customers and products
    count_prior_customer = 10
    customer_count[1] = count_prior_customer

    count_prior_product = 10
    product_count[1] = count_prior_product

    for filepath in files:
        start = datetime.now()

        collection_name = filepath.split(".")[0]

        print("opening", "/".join([data_dir, filepath]))
        with open("/".join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=",")

            header = False
            for row in reader:
                if not header:
                    header = [h.strip("\ufeff") for h in row]
                else:
                    data = {header[i]: v for i, v in enumerate(row)}
                    # print(data)
                    cursor = db[collection_name]
                    try:
                        cursor.insert_one(data)
                        if 'pro' in filepath:
                            product_count[0] += 1
                        # elif: 'pro' in filepath:
                        else:
                            customer_count[0] += 1
                    except Exception as e:
                        print(e)

        end = datetime.now()

        timed = float((end-start).seconds)

        if 'custo' in filepath:
            customer_count[3] = timed
            # add up the count and prior to make a count_new
        if 'pro' in filepath:
            product_count[3] = timed

        return [product_count, customer_count]


def import_data_multithreading(filepath):

    # os.path.basename(filepath).split('.')[0]
    # collection_name = filepath.split(".")[0]

    collection_name = os.path.basename(filepath).split('.')[0]

    print(collection_name)

    customer_count = [0, ]*4
    product_count = [0, ]*4

    # get a prior count of customers and products
    count_prior_customer = 10
    customer_count[1] = count_prior_customer


    print("opening", filepath)
    with open(filepath) as file:
        start = datetime.now()

        reader = csv.reader(file, delimiter=",")

        header = False
        for row in reader:
            if not header:
                header = [h.strip("\ufeff") for h in row]
            else:
                data = {header[i]: v for i, v in enumerate(row)}
                # print(data)
                cursor = db[collection_name]
                try:
                    cursor.insert_one(data)
                    if 'pro' in filepath:
                        product_count[0] += 1
                    else:
                        customer_count[0] += 1
                except Exception as e:
                    print(e)

        end = datetime.now()

        timed = float((end-start).seconds)

        if 'custo' in filepath:
            customer_count[3] = timed
            # add up the count and prior to make a count_new
        if 'pro' in filepath:
            product_count[3] = timed

        return [customer_count, product_count]


def get_product_info(product_id):
    return db["product"].find_one({"product_id": product_id})


def get_rental_info():
    return db["rental"].aggregate([
        {
            "$lookup":
                {
                    "from": "customer",
                    "localField": "user_id",  # what is field name in rental?
                    "foreignField": "Id",  # what is field name in customer?
                    "as": "customer_info"
                }
        },
        {
            "$lookup":
                {
                    "from": "product",
                    "localField": "product_id",  # what is field name in rental?
                    "foreignField": "product_id",  # what is field name in product?
                    "as": "product_info"
                }
        },
    ])


def show_available_products():
    # Returns a Python dictionary of products listed as available with the following fields:
    # product_id.
    # description.
    # product_type.
    # quantity_available.
    # For example:
    # {‘prd001’:{‘description’:‘60-inch TV stand’,’product_type’:’livingroom’,’quantity_available’:‘3’},’prd002’:{‘description’:’L-shaped sofa’,’product_type’:’livingroom’,’quantity_available’:‘1’}}

    output = {}
    for product in db["product"].find():
        output[product["product_id"]] = {
            "description": product["description"],
            "product_type": product["product_type"],
            "qantity_available": product["qantity_available"],  #### MISSPELLING!!!!
        }

    return output


def show_rentals(product_id):
    # Returns a Python dictionary with the following user information from users that have rented products matching product_id:
    # user_id.
    # name.
    # address.
    # phone_number.
    # email.
    # For example:
    # {‘user001’:{‘name’:’Elisa Miles’,’address’:‘4490 Union Street’,’phone_number’:‘206-922-0882’,’email’:’elisa.miles@yahoo.com’},’user002’:{‘name’:’Maya Data’,’address’:‘4936 Elliot Avenue’,’phone_number’:‘206-777-1927’,’email’:’mdata@uw.edu’}}

    rentals = db["rental"].aggregate([
        {
            "$lookup":
                {
                    "from": "customer",
                    "localField": "user_id",  # what is field name in rental?
                    "foreignField": "Id",  # what is field name in customer?
                    "as": "customer_info"
                }
        },
        {
            "$match": {
                "$and": [{"product_id": product_id}]
            }
        },
    ])

    output = {}
    for rental in rentals:
        # DEBUG
        pprint(rental["customer_info"])

        user_id = rental["customer_info"][0]["Id"]
        name = rental["customer_info"][0]["Name"] + " " + rental["customer_info"][0]["Last_name"]
        address = rental["customer_info"][0]["Home_address"]
        phone_number = rental["customer_info"][0]["Phone_number"]
        email = rental["customer_info"][0]["Email_address"]

        output[user_id] = {
            "name": name,
            "address": address,
            "phone_number": phone_number,
            "email": email,
        }

    return output


def linear():
    return import_data("data", "product.csv", "customer.csv")


def parallel():
    return import_data("data", "product.csv", "customer.csv")


if __name__ == "__main__":
    db["customer"].drop()
    db["product"].drop()
    db["rental"].drop()

    import_data("data", "product.csv", "customer.csv", "rental.csv")

    # pprint(get_product_info("P000013"))

    # show_available_products()

    # pprint(show_rentals("P000001"))

    # for rental in get_rental_info():
    #     pprint(rental)

    # def func():
    #     for i in range(5):
    #         print("hello from thread %s" % threading.current_thread().name)
    #         time.sleep(1)

    # files = ["data/product.csv", "data/customer.csv", "data/rental.csv"]
    # threads = []
    # for filepath in files:
    #     thread = threading.Thread(target=import_data_multithreading, args=(filepath,))
    #     thread.start()
    #     threads.append(thread)