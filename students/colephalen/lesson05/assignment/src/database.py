import csv
from pymongo import MongoClient

import threading

mongo = MongoClient("mongodb://localhost:27017")

db = mongo["norton"]


def import_data(data_dir, *files):
    for filepath in files:
        print('opening file: {}'.format(filepath))
        collection_name = filepath.split(".")[0]
        print("creating collection: {}".format(collection_name))

        with open("/".join([data_dir, filepath])) as file:
            reader = csv.reader(file, delimiter=",")

            header = False

            table = db[collection_name]

            for row in reader:
                if not header:
                    header = [h for h in row]
                else:
                    data = {
                        header[i]: v for i, v in enumerate(row)
                    }

                    try:
                        table.insert_one(data)
                    except Exception as e:
                        print(e)

                    # pprint(data)


def import_data_multithread(filepath):
    print('opening file: {}'.format(filepath))
    collection_name = filepath.split(".")[0]
    print("creating collection: {}".format(collection_name))

    with open(filepath) as file:
        reader = csv.reader(file, delimiter=",")

        header = False

        table = db[collection_name]

        for row in reader:
            if not header:
                header = [h for h in row]
            else:
                data = {header[i]: v for i, v in enumerate(row)}

                try:
                    table.insert_one(data)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    db['customer'].drop()
    db['rental'].drop()
    db['product'].drop()
    # import_data('rentals/data', 'customer.csv', 'product.csv', 'rental.csv')

    files = [
        "rentals/data/product.csv",
        "rentals/data/rental.csv",
        "rentals/data/customer.csv"
    ]

    threads = []

    for filepath in files:
        thread = threading.Thread(target=import_data_multithread,
                                  args=(filepath,)
                                  )
        thread.start()
        threads.append(thread)

        # # might not apply:
        for thread in threads:
            thread.join()

