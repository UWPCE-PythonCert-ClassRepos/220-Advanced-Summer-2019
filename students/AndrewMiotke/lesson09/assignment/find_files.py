""" Lesson 09 assignment """

import os
import pprint

data = {}

def find_files(folder, file_extension):
    for item in os.listdir(folder):
        item = "/".join([folder, item])

        if os.path.isdir(item):
            data[item] = []

            # Recursion
            find_files(item, file_extension)
            if len(data[item]) == 0:
                del data[item]
        else:
            if item[-1*len(file_extension):] == file_extension:
                basename = os.path.basename(item)
                dirname = os.path.dirname(item).strip("/")
                data[dirname].append(basename)


find_files(".", ".png")


# Some random homework related stuff
from pymongo import MongoClient

# Just use a context manager
class MongoDBConnection:
    def __init__(self, host="localhost", port="27017"):
        self.host = f"mongodb://{host}:{port}"
        self.connection = None


    def __enter__(self):
        self.connection = MongoClient(self.host)
        return self


    def __exit__(self, a, b, c):
        self.connection.close()
        self.connection.disconnect()

    with MongoDBConnection() as mongo:
        conn = mongo.connection
        db = conn.my_app
        collection = db.people

        collection.insert_many([
            {
                "tests/lesson09/data/furniture/chair": [
                    "metal_chair_back_isometric_400_clr_17527.png"
                ],
                "tests/lesson09/data/furniture/chair/couch": [
                    "sofa_400_clr_10056.png"
                ],
                "tests/lesson09/data/furniture/table": [
                    "basic_desk_main_400_clr_17523.png",
                    "desk_isometric_back_400_clr_17524.png",
                    "table_with_cloth_400_clr_10664.png"
                ],
                "tests/lesson09/data/new": [
                    "chairs_balancing_stacked_400_clr_11525.png",
                    "hotel_room_400_clr_12721.png"
                ],
                "tests/lesson09/data/old": [
                    "couple_on_swing_bench_400_clr_12844.png",
                    "sitting_in_chair_relaxing_400_clr_6028.png"
                ]
            }
        ])

        person = collection.find({"first_name": "Lisetta"})
        pprint(list(person))
