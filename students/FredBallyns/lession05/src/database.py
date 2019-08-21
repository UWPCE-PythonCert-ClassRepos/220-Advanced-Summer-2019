import csv
from pymongo import MongoClient



def import_data(data_dir, *files):
    for filepath in files:
        print(f"opening files: {filepath}")
        collection_name = filepath.split(".")[0]

        with open("/".join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=",")

            table = db[collection_name]

            header = []
            for row in reader:
                if not header:
                    header = [h for h in row]
                else:
                    data = {header[i]: val for i, val in enumerate(row)}
                    try:
                        table.insert_one(data)
                    except Exception as e:
                        print(e)


if __name__== "__main__":
    mongo = MongoClient("mongodb://localhost:27017")
    db = mongo["norton"]
    """
    db["customer"].drop()
    db["rental"].drop()
    db["product"].drop()"""
    import_data("../data", "customer.csv", "rental.csv", "product.csv")
    mongo.close
