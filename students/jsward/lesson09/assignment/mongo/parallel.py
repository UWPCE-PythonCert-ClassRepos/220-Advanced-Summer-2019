# They are not, in fact, constants...
# pylint: disable=C0103

# pylint: disable=W0703
"""
Lesson 7: Parallel
Relational concept  Mongo DB equivalent
Database	        Database
Tables	            Collections
Rows	            Documents
Index	            Index
"""

import csv
import datetime
import logging
import sys
import threading
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

list_of_tuples = []


class MongoDBConnection:
    """Context manager for MongoDB connections"""
    def __init__(self, host="localhost", port="27017"):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def populate_collection(db_name, data_dir, file_path):
    """ Imports data from file_path into collection """
    with MongoDBConnection() as connection:
        thread_assignment_db = connection.connection[db_name]  # MongoClient(connection_string)[db_name]
        processed = 0
        collection_name = file_path.split(".")[0]
        try:
            count_prior = sum(1 for _ in thread_assignment_db[collection_name].find())
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
                        thread_assignment_db[collection_name].insert_one(data)
                        processed += 1
                        logger.debug("Inserted record %s into collection %s", data, collection_name)
                    except pymongo_errors.ServerSelectionTimeoutError as ex:
                        logger.error("Timeout or connection refused when connecting to MongoDB: %s", ex)
                        continue
                    except Exception as ex:
                        logger.error("Error inserting record %s into table %s in MongoDB %s Error: %s",
                                     data, thread_assignment_db.name, connection.connection, ex)
                        continue
    list_of_tuples.append(tuple([processed, count_prior, (count_prior + processed), (time.time() - start_time)]))
    logger.info("Inserted %s records into collection %s in %s", processed, collection_name, (time.time() - start_time))
    logger.info("Collection now contains %s records", (count_prior + processed))


def import_data(data_dir, *files):
    """ Imports data from file(s) to mongodb"""
    threads = [threading.Thread(target=populate_collection, args=("assignment", data_dir, fp)) for fp in files]
    [thread.start() for thread in threads]  # pylint: disable=W0106
    [thread.join() for thread in threads]  # pylint: disable=W0106
    return list_of_tuples


if __name__ == "__main__":
    # results = import_data('data', 'customers.csv', 'products.csv')
    # print(results)
    pass
