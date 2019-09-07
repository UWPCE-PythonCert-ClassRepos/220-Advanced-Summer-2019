# They are not, in fact, constants...
# pylint: disable=C0103

# pylint: disable=W0703
"""
Lesson 7: Linear
Relational concept  Mongo DB equivalent
Database	        Database
Tables	            Collections
Rows	            Documents
Index	            Index
"""

import cProfile
import csv
import datetime
import logging
import sys
import time

from pymongo import MongoClient
from pymongo import errors as pymongo_errors

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("mongo_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

mongo_client = MongoClient("mongodb://localhost:27017")
assignment_db = mongo_client["assignment"]


def import_data(data_dir, *files):
    """ Imports data from file(s) to mongodb"""
    list_of_tuples = []
    for file_path in files:
        processed = 0
        collection_name = file_path.split(".")[0]
        try:
            count_prior = sum(1 for _ in assignment_db[collection_name].find())
        except Exception:
            logger.info("No existing records found in collection %s", collection_name)
            count_prior = 0
        with open("/".join([data_dir, file_path])) as file:
            reader = csv.reader(file, delimiter=",")
            header = False
            start_time = time.time()
            for row in reader:
                if not header:
                    header = [h.strip("\ufeff") for h in row]
                else:
                    data = {header[i]: v for i, v in enumerate(row)}
                    try:
                        assignment_db[collection_name].insert_one(data)
                        processed += 1
                        logger.debug("Inserted record %s into collection %s", data, collection_name)
                    except pymongo_errors.ServerSelectionTimeoutError as ex:
                        logger.error("Timeout or connection refused when connecting to MongoDB: %s", ex)
                        break
                    except Exception as ex:
                        logger.error("Error inserting record %s into table %s in MongoDB %s Error: %s",
                                     data, assignment_db.name, mongo_client, ex)
                        continue
        end_time = time.time()
        list_of_tuples.append(tuple([processed, count_prior, (count_prior + processed), (end_time - start_time)]))
        logger.info("Inserted %s records into collection %s in %s", processed, collection_name, (end_time - start_time))
        logger.info("Collection now contains %s records", (count_prior + processed))
    return list_of_tuples


if __name__ == "__main__":
    import_data('data', 'customers.csv', 'products.csv')
    # print(results)

