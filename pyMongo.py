# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:31:28 2023

@author: ASUS
"""

import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = conn.mydb

print(conn.list_database_names())

collection = mydb.KuchindaCollege

# collection.delete_many({})

collection.update_one({'mobile': 9482840453}, {"$set": {'name': 'Sumit Patel', 'email': 'sumit.patel.iisc@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9480350453}, {"$set": {'name': 'Suprita Patel', 'email': 'suprita91@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9482547149}, {"$set": {'name': 'Amit Patel', 'email': 'amit.patel.atos@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 7873670001}, {"$set": {'name': 'Adesh Patel', 'email': 'adesh.patel@gmail.com'}}, upsert=True)
collection.update_one({'mobile': 9348536104}, {"$set": {'name': 'Prasanna Patel', 'email': 'prasanna.patel@gmail.com'}}, upsert=True)

myquery = {"email":"adesh.patel@gmail.com"}
filtered = collection.find(myquery)
for x in filtered:
    print(x)
    
print("---------------")
myquery = {"email":"sumit.patel.iisc@gmail.com"}
filtered = collection.find(myquery)
for x in filtered:
    print(x)