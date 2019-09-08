"""
As a HP Norton customer I want to see a list of all products available for rent so that I can make a rental choice.

As a HP Norton salesperson I want to see a list of all of the different products, showing product ID, description, product type and quantity available.

As a HP Norton salesperson I want to see a list of the names and contact details (address, phone number and email) of all customers who have rented a certain product.
"""

from pymongo import MongoClient
from pprint import pprint

import csv

#client = MongoClient('mongodb://%s:%s@localhost:27017' % ('admin','password'))
client = MongoClient('mongodb://localhost:27017')
db = client.nortonDB
# db = client.admin


def import_data(data_dir, files):
    record_count = [0,0,0]
    error_count = [0,0,0]
    for index, filepath in enumerate(files):
        print("Opening file %s" %filepath)
        collection_name = filepath.split('.')[0]
        print("Creating collection %s" %collection_name)
        with open('/'.join([data_dir, filepath]), encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file, delimiter=',')
            header = False
            for row in csv_reader:
                if not header:
                    header = [h for h in row]
                else:
                    data = {
                        header[i]:v
                        for i,v in enumerate(row)
                    }

                    table = db[collection_name]
                    record_count[index] += 1
                    try:
                        table.insert_one(data)
                    except Exception as e:
                        print(e)
                        error_count[index] += 1
                    #pprint(data)
    return tuple(record_count),tuple(error_count)

def show_available_products():
    column = db["product"]
    query = {'quantity_available':{'$gt':"0"}} # why the 0 needs to be in the quotes?
    result = iter(column.find(query))
    result_dict = {}
    for product in result:
        product_id = product["product_id"]
        description = product["description"]
        product_type = product["product_type"]
        quantity_available = product["quantity_available"]
        result_dict.update({product_id:{"description":description, "product_type":product_type,
                                    "quantity_available":quantity_available}})
    return result_dict


def list_unique_products():
    products = db["product"].distinct('product_id')
    result = {}
    for product in products:
        product_info = db["product"].find_one({"product_id":{'$eq':product}})
        product_id = product
        description = product_info["description"]
        product_type = product_info["product_type"]
        quantity_available = product_info["quantity_available"]
        result.update({product_id:{"description":description, "product_type":product_type,
                                    "quantity_available":quantity_available}})
    return result

def show_rentals(product_id):
    rentals = db['rental']
    users = db['customers']
    query = {"product_id":{"$eq":product_id}}
    userswithrentals = rentals.find(query)
    result = {}
    for user in userswithrentals:
        user_id = user['user_id']
        query = {"user_id":{"$eq":user_id}}
        user_info = users.find(query)[0]
        name = user_info['name']
        address = user_info['address']
        phone = user_info['phone_number']
        email = user_info['email']
        result.update({user_id:{"name":name,"address":address,"phone_number":phone,"email":email}})
    return result


if __name__ == "__main__":
    db.drop_collection("product")
    db.drop_collection("rental")
    db.drop_collection("customers")

    files = [
        "customers.csv",
        "product.csv",
        "rental.csv",
    ]
    print(import_data('data', files))
    print(show_available_products())
    print(show_rentals('prd001'))
    print(list_unique_products())
    print('Done!')