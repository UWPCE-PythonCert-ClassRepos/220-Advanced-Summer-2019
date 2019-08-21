""" DynamoDB Example """

import csv
import threading
import boto3
from pprint import pprint

session = boto3.Session(profile_name='default')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


def dynamo_create_table(table_name, key_schema, attribute_definitions):
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print("table created")
        return True
    except Exception as e:
        print(e)
        return False


def import_data_multithreaded(file_path):
    print(f'opening file: {file_path}')
    collection_name = file_path.split('/')[-1].split('.')[0]
    print(f'creating collection: {collection_name}')

    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')

        header = False


        for row in reader:
            if not header:
                header = [h for h in row]

                dynamo_create_table(
                    collection_name,
                    [
                        {
                            'AttributeName': header[0],
                            'KeyType': 'HASH',
                        }
                    ],
                    [
                        {
                            'AttributeName': header[0],
                            'AttributeType': 'S',
                        }
                    ],
                )
            else:
                data = {header[column]:value for column,value in enumerate(row)}
                print(data)
            try:
                dynamodb.Table(collection_name).put_item(Item=data)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    files = [
        'data/product.csv',
        'data/rental.csv',
        'data/customer.csv',
    ]

    threads = []

    for file_path in files:
        thread = threading.Thread(target=import_data_multithreaded, args=(file_path,))
        thread.start()
        threads.append(thread)
