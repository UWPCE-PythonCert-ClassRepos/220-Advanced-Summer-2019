"""
    You will submit two modules: linear.py and parallel.py
    Each module will return a list of tuples, one tuple for
     customer and one for products.
    Each tuple will contain 4 values: the number of records processed,
    the record count in the database prior to running, the record count
    after running,
    and the time taken to run the module.

"""


import csv
from pprint import pprint
from pymongo import MongoClient
import threading
import logging
import time
import sys

mongo = MongoClient("mongodb://localhost:27017")
db = mongo.norton

def import_data_multithreaded(data_dir, file):
    
    print("opening file %s" % file)
    collection_name = file.split('.')[0]
    print("creating collection %s" % collection_name)
    prev_count = db[collection_name].count_documents({})
    record_count = 0
    with open('/'.join([data_dir, filepath])) as file:
        reader = csv.reader(file, delimiter=',')
        header = False
        for row in reader:
            if not header:
                header = [h for h in row]
            else:
                data = {
                    header[i]:v 
                    for i,v in enumerate(row)
                }
                
                table = db[collection_name]
                try:
                    table.insert_one(data)
                    record_count += 1
                except Exception as e:
                    print(e)
    end = time.time()
    global elapsed
    if end - start > elapsed:
        elapsed = end - start
    after_count = db[collection_name].count_documents({})
    result = (elapsed, prev_count, record_count, after_count)
    print(result)
    return result


if __name__ == "__main__":
    db["customer"].drop()
    db["product"].drop()
    db["rental"].drop()
    start = time.time()
    elapsed = 0
    files = [
        "product.csv",
        "customer.csv",
        "rental.csv"
    ]
    threads = []
    for filepath in files:
        thread = threading.Thread(
            target=import_data_multithreaded,
            args=('data', filepath,)
        )
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

