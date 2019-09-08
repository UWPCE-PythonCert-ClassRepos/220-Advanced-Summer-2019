from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host="localhost", port="27017"):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self

    def __exit__(self, a, b, c):
        self.connection.close()


with MongoDBConnection() as mongo:
    conn = mongo.connection
    db = conn.my_app
    collection = db.people
    data = [
        {"name": "Jeremy Jay",
         "age": 23},
        {"name": "Michael James",
         "age": 40}
    ]
    collection.insert_many(data)

    jeremy = collection.find_one({"name": "Jeremy Jay"})
    if jeremy:
        age = jeremy["age"]
        print(f"Jeremy found, age: {age}")
    else:
        print("Jeremy not found")


