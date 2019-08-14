import csv

mongo = MongoClient("mongodb://localhost:27017")
db = mongo["assignment"]

def import_data(data_dir, *files):
    for filepath in files:
        collection_name = filepath.split("."[0])
        print("opening ", "/".join([data_dir, filepath]))
        with open("/".join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=",")

            header = False
            for row in reader:
                if not header:
                    header = [h.strip("\ufeff") for h in row]
                else:
                    data = {header[i]:v for i, v in enumerate(row)}
                    print(data)
                    cursor = db[collection_name]
                    cursor.insert_one(data)

import_data("assingment/data",  "products.csv", "customers.csv", "rentals.csv")

