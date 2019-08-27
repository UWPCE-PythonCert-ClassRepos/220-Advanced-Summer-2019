import csv
import os.path
from pymongo import MongoClient

mongo = MongoClient("localhost:27017")

db = mongo["norton"]


def import_data(data_dir, *files):
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
    rental_col = db["rental"]
    customers_col = db["customers"]
    query = {"ï»¿product_id":{"$eq":product_id}}
    users_with_rentals = rental_col.find(query)
    rentals_dict = {}
    for user in users_with_rentals:
        usr_id = user['user_id']
        query = {"ï»¿user_id":{"$eq":usr_id}}
        user_info = customers_col.find(query)[0]
        name = user_info["name"]
        address = user_info["address"]
        phone_number = user_info["phone_number"]
        email = user_info["email"]
        rentals_dict.update({usr_id:{"name":name, "address":address, "phone_number":phone_number, "email": email}})
    return rentals_dict


if __name__ == '__main__':
    db.drop_collection("product")
    db.drop_collection("customers")
    db.drop_collection("rental")

    show_available_products()
    show_rentals('prd006')
    show_rentals('prd002')