"""
context managers in class
"""

# with open('some.txt', 'w') as file:
#     pass
#
# file.write('dir dir dir')


# class C:
#     def __init__(self):
#         print("initializing context manager")
#         self.x = 0
#
#     def __enter__(self):
#         print('entering context manager')
#         self.x = 5
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exiting context manager')
#         self.x = -1
#
#
# print('do work')
# with C() as c:
#     print(c.x)
# print('continue work')

from pymongo import MongoClient
from pprint import *


class MongoDBConnection:
    """MongoDB Connection"""
    def __init__(self, host='localhost', port='27017'):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


with MongoDBConnection() as mongo:
    conn = mongo.connection
    db = conn.my_app
    collection = db.people

    collection.delete_many({})

    collection.insert_many([
        {
            "first_name": "Lisetta",
            "last_name": "Bennitt",
            "email": "lbennitt0@typepad.com"
        }, {
            "first_name": "Maurits",
            "last_name": "Trazzi",
            "email": "mtrazzi1@mysql.com"
        }, {
            "first_name": "Mandel",
            "last_name": "Handover",
            "email": "mhandover2@weebly.com"
        }
    ])

    # find person
    person = collection.find({"first_name": "Mandel"})
    pprint(list(person))


"""
from pymongo import MongoClient

# https://medium.com/@ramojol/python-context-managers-and-the-with-statement-8f53d4d9f87

class MongoDBConnection(object):
    def __init__(self, host='localhost', port='27017'):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None
    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        
        
# docker container run --name mongo -p 27017:27017 -d mongo mongod

with MongoDBConnection() as mongo:
    conn = mongo.connection
    db = conn.my_app
    collection = db.people
    
    # clear the deck
    collection.delete_many({})
    
    # insert data
    collection.insert_many([
        {
          "first_name": "Lisetta",
          "last_name": "Bennitt",
          "email": "lbennitt0@typepad.com"
        }, {
          "first_name": "Maurits",
          "last_name": "Trazzi",
          "email": "mtrazzi1@mysql.com"
        }, {
          "first_name": "Mandel",
          "last_name": "Handover",
          "email": "mhandover2@weebly.com"
        }
    ])
    
    # find person
    person = collection.find({"first_name":"Mandel"})
    pprint(list(person))

"""