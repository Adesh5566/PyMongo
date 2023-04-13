# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:31:28 2023

@author: Adesh Patel
"""

import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = conn.mydb

print(conn.list_database_names())

collection = mydb.KuntraCollege

# collection.delete_many({})

collection.update_one({'mobile': 9444444444}, {"$set": {'name': 'Sumit Patel', 'email': 'sumit.xxxx@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9555555555}, {"$set": {'name': 'Suprita Patel', 'email': 'suprita.xxxx@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9666666666}, {"$set": {'name': 'Amit Patel', 'email': 'amit.xxxx@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 7777777777}, {"$set": {'name': 'Adesh Patel', 'email': 'adesh.xxxx@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9888888888}, {"$set": {'name': 'Prasanna Patel', 'email': 'prasanna.xxxx@gmail.com'}}, upsert=True)

myquery = {"email":"adesh.patel@gmail.com"}
filtered = collection.find(myquery)
for x in filtered:
    print(x)
    
print("---------------")
myquery = {"email":"sumit.patel.iisc@gmail.com"}
filtered = collection.find(myquery)
for x in filtered:
    print(x)