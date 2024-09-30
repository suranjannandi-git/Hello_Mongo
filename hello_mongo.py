from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def check_mongodb_status(mongo_uri):
    try:
        # Create a MongoClient to the running MongoDB instance
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        
        # Attempt to retrieve the server information
        client.admin.command('ping')
        print("MongoDB is running.")

        return client
    
    except ConnectionFailure as e:
        print(f"MongoDB is not running: {e}")

def get_collection(client):
    # Access the database
    db = client.mongo_db1  #replace 'mongo_db' with any other database name

    # Access a collection
    collection = db.mongo_collection  # replace 'mongo_collection' with any other collection name
    return collection

def insert_one_into_collection(collection, document):
    result = collection.insert_one(document)

    # Example: Query the collection
    for doc in collection.find():
        print(doc)

def insert_many_into_collection(collection, documents):
    # Insert multiple documents
    result = collection.insert_many(documents)

    # Print the inserted IDs
    print(f'Documents inserted with IDs: {result.inserted_ids}')

    # Verify the insertion by querying the collection
    for doc in collection.find():
        print(doc['name'])





if __name__ == "__main__":
    mongo_uri = 'mongodb://192.168.29.217:27017/'
    client = check_mongodb_status(mongo_uri)

    collection = get_collection(client)
    print(collection)

    # Example: Insert a document into the collection
    document = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    insert_one_into_collection(collection, document)
    
    # List of documents to insert
    documents = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    insert_many_into_collection(collection, documents)
