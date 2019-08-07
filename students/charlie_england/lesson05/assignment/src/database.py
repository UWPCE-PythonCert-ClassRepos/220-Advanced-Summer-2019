import csv
import os.path
from pymongo import MongoClient

mongo = MongoClient("localhost:27017")

db = mongo["hp_norton"]
db.drop_collection("product")
db.drop_collection("customers")
db.drop_collection("rental")

def import_data(data_dir, *files):
    """
        given a directory and files
    """
    added = [0, 0, 0]
    errors = [0, 0, 0]
    reference = 0
    for filepath in files:
        collection_name = filepath.split(".")[0]
        with open(os.path.join(data_dir, filepath)) as file:
            reader = csv.reader(file, delimiter=",")
            header = False

            for row in reader:
                try:
                    if not header:
                        header = [h.strip("\ufeff") for h in row]
                    else:
                        data = {header[i]:v for i, v in enumerate(row)}
                        cursor = db[collection_name]
                        cursor.insert_one(data)
                        added[reference] +=1
                except Exception:
                    errors[reference] += 1
            reference += 1
    return tuple(added), tuple(errors)

def show_available_products():
    """
        Returns a Python dictionary of products listed as available with the following fields:
        product_id.
        description.
        product_type.
        quantity_available.
        For example: {‘prd001’:{‘description’:‘60-inch TV stand’,
        ’product_type’:’livingroom’,’quantity_available’:‘3’},
        ’prd002’:{‘description’:’L-shaped sofa’,
        ’product_type’:’livingroom’,’quantity_available’:‘1’}}
    """
    col = db["product"]
    query = {"quantity_available":{"$gt":"0"}}
    final_dict = {}
    available_products = iter(col.find(query))
    for product in available_products:
        prod_id = product["ï»¿product_id"]
        description = product["description"]
        product_type = product["product_type"]
        quantity_available = product["quantity_available"]
        final_dict.update({prod_id:{"description":description, "product_type":product_type,
                                    "quantity_available":quantity_available}})
        final_dict.update({prod_id:{"description":description, "product_type":product_type,
                                    "quantity_available":quantity_available}})
    return final_dict

def show_rentals(product_id):
    """
        show_rentals(product_id): Returns a Python dictionary with
        the following user information from users that have rented
        products matching product_id:
        user_id.
        name.
        address.
        phone_number.
        email.
        For example: {‘user001’:{‘name’:’Elisa Miles’,’address’:‘4490 Union Street’,
        ’phone_number’:‘206-922-0882’,’email’:’elisa.miles@yahoo.com’},
        ’user002’:{‘name’:’Maya Data’,’address’:‘4936 Elliot Avenue’,’phone_number’:‘206-777-1927’,
        ’email’:’mdata@uw.edu’}}
    """
    rental_col = db["rental"]
    customers_col = db["customers"]
    query = {"ï»¿product_id":{"$eq":product_id}}
    users_with_rentals = rental_col.find(query)
    rentals_dict = {}
    print(product_id)
    print(query)
    for user in users_with_rentals:
        usr_id = user['user_id']
        print(user)
        print(user["user_id"])
        query = {"ï»¿user_id":{"$eq":usr_id}}
        user_info = customers_col.find(query)[0]
        name = user_info["name"]
        address = user_info["address"]
        phone_number = user_info["phone_number"]
        email = user_info["email"]
        rentals_dict.update({usr_id:{"name":name, "address":address, "phone_number":phone_number, "email": email}})
    return rentals_dict
