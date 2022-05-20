from pymongo import MongoClient
import pprint


class DataBase:
    def __init__(self, host, port, db, collection):
        self.client = MongoClient(host, port)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def find_all(self):
        for element in self.collection.find():
            print(element)

    def find_by_name(self, name):
        for element in self.collection.find({'name': name}):
            print(element['name'], element['age'])


    def insert_one(self, element):
        self.collection.insert_one(element)
    
    def insert_many(self, elements):
        self.collection.insert_many(elements)

database = DataBase(
    host='localhost',
    port=27017,
    db='test',
    collection='users')
#database.insert_one({'name': 'Alice', 'age': 40})
#database.insert_many([{'name': 'Fred', 'age':11}, {'name':'Alex', 'age':21}])
database.find_all()
database.find_by_name('Alice')