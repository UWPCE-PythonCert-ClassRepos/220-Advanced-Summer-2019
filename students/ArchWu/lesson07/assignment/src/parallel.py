import csv
from pprint import pprint
from pymongo import MongoClient
import threading
import logging

mongo = MongoClient("mongodb://localhost:27017")
db = mongo.norton

                    
# def dynamo_create_table(table_name, key_schema, attribute_definitions):
#     try:
#         table = dynamodb.create_table(
#             TableName=table_name,
#             KeySchema=key_schema,
#             AttributeDefinitions=attribute_definitions,
#             ProvisionedThroughput={
#                 "ReadCapacityUnits": 5,
#                 "WriteCapacityUnits": 5,
#             }
#         )
#         table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
#         print("table created")
#         return True
#     except Exception as e:
#         logging.error("Error")

def import_data_multithreaded(data_dir, file):
    
    print("opening file %s" % file)
    collection_name = file.split('.')[0]
    print("creating collection %s" % collection_name)

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
                except Exception as e:
                    print(e)
                #pprint(data)

def import_data(data_dir, files):
    for filepath in files:
        print("opening file %s" % filepath)
        collection_name = filepath.split('.')[0]
        print("creating collection %s" % collection_name)

        with open('/'.join([data_dir,filepath])) as file:
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
                    except Exception as e:
                        print(e)
                    pprint(data)

if __name__ == "__main__":
    db["customer"].drop()
    db["product"].drop()
    db["rental"].drop()

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
