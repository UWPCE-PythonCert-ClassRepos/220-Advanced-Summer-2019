import csv
import threading
# from multiprocessing.pool import ThreadPool
import multiprocessing
from pymongo import MongoClient


def gen_chunks(reader, headers, chunksize=100):
    """
    Chunk generator. Take a CSV `reader` and yield
    `chunksize` sized slices.
    """
    chunk = []
    for index, line in enumerate(reader):
        if index % chunksize == 0 and index > 0:
            yield chunk
            del chunk[:]
        data = {headers[i]: v for i, v in enumerate(line)}
        chunk.append(data)
    yield chunk


class ParallelInsert:
    def __init__(self, database, process_pool):
        self.db = database
        self.workers = process_pool
        self.chunks = []
        self.tables = []
        self.all_threads = []

    def insert_to_db(self):
        chunk = self.chunks[0]
        self.chunks.pop(0)
        table_name = self.tables[0]
        self.tables.pop(0)

        cursor = self.db[table_name]
        for data in chunk:
            print("inserting " + str(data) + " to " + table_name)
            cursor.insert_one(data)

    def split_and_import(self, data_dir, file_name):
        print("Opening ", "\\".join([data_dir, file_name]))

        collection_name = file_name.split(".")[0]

        with open("\\".join([data_dir, file_name])) as file:
            reader = csv.reader(file, delimiter=",")

            header_cols = []
            header = next(reader)
            for h in header:
                # this is for striping any unicode code point > 128 (aka.non ASCII)
                col = ''.join([i if ord(i) < 128 else "" for i in h])
                header_cols.append(col)
                print("col=" + col)

            print(f"header_cols={header_cols}")
            chunks = gen_chunks(reader, header_cols)
            for chunk in chunks:
                self.chunks.append(chunk)
                self.tables.append(collection_name)
                worker_thread = threading.Thread(target=self.insert_to_db)
                worker_thread.start()
                self.all_threads.append(worker_thread)

                #self.workers.map(self.insert_to_db, [])

        print("Finished importing " + "\\".join([data_dir, file_name]))


    def import_data(self, data_dir, *files):
        #tasks = []
        for file_path in files:
            #task = threading.Thread(target=split_and_import, args=[data_dir, file_path])
            #tasks.append(task)
            #task.start()
            self.split_and_import(data_dir, file_path)

    def show_available_products(self):
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

    def show_rentals(self, product_id):
        customers = {}
        for rental in db.rental.find({"product_id": product_id}):
            customer = db.customers.find_one({"user_id": rental["user_id"]})
            if customer:
                print(customer)
                customers[customer["Id"]] = {
                    "name": customer["Name"],
                    "address": customer["Home_address"],
                    "phone_number": customer["Phone_number"],
                    "email": customer["Email"]
                }
        print("Rentals for product_id:" + product_id + ":")
        print(customers)
        print("\n")


if __name__ == "__main__":
    mongo = MongoClient("mongodb://localhost:27017")
    db = mongo["assignment"]
    mongo.drop_database("assignment")

    workers = multiprocessing.Pool(processes=8)

    inserter = ParallelInsert(db, workers)

    inserter.import_data("data", "product.csv", "customer.csv", "rental.csv")

    for thread in inserter.all_threads:
        thread.join()

    print("\n\n\n*******All available products********")
    inserter.show_available_products()
    print("\n\n\n*******All rentals for P000008********")
    inserter.show_rentals('P000008')
    print("\n\n\n*******All rentals for P009989********")
    inserter.show_rentals('P009989')

    mongo.drop_database("assignment")





