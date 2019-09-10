import csv
from pprint import pprint
from pymongo import MongoClient
import threading
import boto3

mongo = MongoClient("mongodb://localhost:27017")
db = mongo["norton"]
dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
def import_data_multithreaded(data_dir, *files):
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
                    
def dynamo_create_table(table_name, key_schema, attribute_definitions):
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            }
        )
        table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
        print("table created")
        return True

def import_data_multithreaded(data_dir, *files):
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

def import_data(data_dir, *files):
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
    db["rentals"].drop()

    files = [
        "data/product.csv",
        "data/customer.csv",
        "data/rental.csv"
    ]
    threads = []
    for filepath in files:
        thread = threading.Thread(
            target=import_data_multithreaded,
            args=(filepath,)
        )
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    
    # import_data("data", "customer.csv", "product.csv", "rental.csv")