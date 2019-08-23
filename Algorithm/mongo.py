from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://number1:1234@engagement-montor-9t1qi.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["engagement-montor"]
collection = db["Admin"]

post = {"Name":"Sandy","Pass":"Manboobs"}

print(collection.insert_one(post))

