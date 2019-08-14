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
    query = {"quantity_available" : >0}  #show all products with quant > 0
    available_products = products.find(query)
    print(available_products)
    return available_products


def show_rentals(rentals, customers):
    # db query to show rented products
    # combines the cusomter collection and product collection

    rentals_query = {"product_id" : "user_id"}
    rented_items = rentals.find(rentals_query)

    # now look through this list to match rented products with users
    list(rented_items)
    for "product_id" in list(rented_items):
        customer_query = {"user_id" : "name"}
        



import_data("assignment/data", "product.csv", "customers.csv", "rental.csv")

if __name__ == "__main__()":
    pass
