from pymongo import MongoClient

# Connect to MongoDB

client = MongoClient('mongodb+srv://master:1234678@test-mongo-svc.mongo-operator.svc.cluster.local/admin?replicaSet=test-mongo&ssl=false')

#create  a database in mongo

list_of_db = client.list_database_names()

print(list_of_db)

db = client['test']

# Get the collection

collection = db['test']

# Insert a document

for i in range(10):

    collection.insert_one({'name': f'{i}+test'})

# Find a document

collection.find_o({'name': 'test'})