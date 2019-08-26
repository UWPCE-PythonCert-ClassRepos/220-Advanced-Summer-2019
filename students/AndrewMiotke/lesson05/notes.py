""" Notes and code """

#     Mongodb
# Mongo uses BSON, similar to JSON
# You can store multiple data types in a mongodb,
# even lists within a data set(dict)


#     CRUD
# Create
# Read
# Update
# Delete

# =============================================================================================================

from pymongo import MongoClient
from random import randint

# pass in the url for the database
# CLIENT
mongo = MongoClient('mongodb://localhost:27017')

# CREATE DATABASE
db = mongo["ecommerce_store"]

# Mongo has collections vs tables in SQL
# TABLE == COLLECTION
customers = db["customer"]

# DOCUMENT == ROW
row = {
    "first_name": "Sam",
    "last_name": "Adams",
    "occupation": "Beverage maker",
    "city": "Boston"
}

# Similar to SQL's create()
# --- CREATE ---
results = customers.insert_one(row)

if results.acknowledged:
    print(results.inserted_id)


# Insert multiple rows
rows = [
        {"first_name": "Sam", "last_name": "Adams", "occupation": "Beverage maker", "city": "Boston"},
        {"first_name": "Sam2", "last_name": "Adams", "occupation": "Beverage maker2", "city": "Boston2"},
        {"first_name": "Sam3", "last_name": "Adams", "occupation": "Beverage maker3", "city": "Boston3"},
        {"first_name": "Sam4", "last_name": "Adams", "occupation": "Beverage maker4", "city": "Boston4"},
        {"first_name": "Sam5", "last_name": "Adams", "occupation": "Beverage maker5", "city": "Seattle"},
        {"first_name": "Sam6", "last_name": "Adams", "occupation": "Beverage maker6", "city": "seattle"} # lower case does work but capitalizes the 's'
]

results = customers.insert_many(rows)
if results.acknowledged:
    print(results.inserted_ids)


# --- READ ---
customers.find()
# returns a cursor object
# cursors are a sort of Generator or Iterator

# Write a query to find any row that contains "city": "Seattle"
where = {"city": "Seattle"}
seattlites = customers.find(where)
print(list(seattlites))

# --- UPDATE ---

# find any row with the keys's value
where = {
    "last_name": "Adams"
}

# update the where value's city
update = {
    "$set": {"city": "San Francisco"}
}

results = customers.update_many(where, update)

where = {
    "city": "Seattle"
}

update = {
    "$set": {"occupation": "Developer"}
}

d = customers.update_many(where, update)
print(d)

where = {
    "last_name": "Adams"
}

# update the where value's city
update = {
    "$set": {"age": randint(25,45)}
}

age_results = customers.update_many(where, update)
list(d)

list(customers.find({
    "age": {"$gt": 32}, # list everyone with an age greater than 32
    "occupation": {"$eq": "developer"} # list everyone with an occupation == "developer"
}))

# --- DELETE ---

where = {
    "city": "Seattle",
    "last_name": "Davis"
}

customers.delete_many(where)

for customer in customers.find():
    print(customer)
