import csv

from pymongo import MongoClient

mongo = MongoClient("mongodb://localhost:27017")
db = mongo["assignment"]


def import_data(data_dir, *files):  # using args to import the multiple csv files
    # should return a count of the number of products, customer,
    # and rentals added - in that order
    # should also return errors of any while adding to db (in that order)
    for filepath in files:
        collection_name = filepath.split(".")[0]

        print("opening", "/".join([data_dir, filepath]))
        with open("/".join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=",")

            header = False
            for row in reader:
                try:  # hey maybe we should do some error handling
                    if not header:
                        header = [h.strip("\ufeff") for h in row]
                    else:
                        data = {header[i]: v for i, v in enumerate(row)}
                        print(data)
                        cursor = db[collection_name]
                        cursor.insert_one(data)
                except Exception as e:
                    print(e)
                    print(f"Could not add {row}" to database)

def show_available_prodcuts(products):
    # DB query and display all

    available_products = products.find(*)
    return available_products


def show_rentals(rentals):
    # db query to show all rentals
    available_rentals = rentals.find(*)
    return available_rentals


import_data("assignment/data", "product.csv", "customers.csv", "rental.csv")

if __name__ == "__main__()":
    pass
