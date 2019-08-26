import csv
from pymongo import MongoClient

mongo = MongoClient("mongodb://localhost:27017")
db = mongo["assignment"]


def import_data(data_dir, *files):
    for file_path in files:
        collection_name = file_path.split(".")[0]

        # print("opening", "\\".join([data_dir, filepath]))
        with open("\\".join([data_dir, file_path])) as file:
            reader = csv.reader(file, delimiter=",")

            header = []
            for row in reader:
                if not header:
                    for h in row:
                        # this is for striping any unicode code point > 128 (aka.non ASCII)
                        col = ''.join([i if ord(i) < 128 else "" for i in h])
                        header.append(col)
                else:
                    data = {header[i]: v for i, v in enumerate(row)}
                    cursor = db[collection_name]
                    print("inserting " + str(data) + " to " + collection_name)
                    cursor.insert_one(data)


def show_available_products():
    all_items = db["product"].find({})
    output = {}
    for each in all_items:
        output[each['product_id']] = {
            "description": each["description"],
            "product_type": each["product_type"],
            "quantity_available": each["quantity_available"]
        }
    print("All available products:")
    print(output)
    print("\n")


def show_rentals(product_id):
    customers = {}
    for rental in db.rental.find({"product_id": product_id}):
        customer = db.customers.find_one({"user_id": rental["user_id"]})
        customers[customer["user_id"]] = {
            "name": customer["name"],
            "address": customer["address"],
            "phone_number": customer["phone_number"],
            "email": customer["email"]
        }
    print("Rentals for product_id:" + product_id + ":")
    print(customers)
    print("\n")


import_data("data", "product.csv", "customers.csv", "rental.csv")
show_available_products()
show_rentals('prd006')
show_rentals('prd002')

mongo.drop_database("assignment")





