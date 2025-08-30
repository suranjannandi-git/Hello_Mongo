import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def check_mongodb_status():
    mongodb_uri = os.getenv("MONGODB_URI")
    mongodb_certificate_path = os.getenv("MONGODB_CERTIFICATE_PATH")

    try:
        # For localhost, we need not require certificate, may need to toggle the client   
        if "localhost" in mongodb_uri or "127.0.0.1" in mongodb_uri:
            client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)
        else:
            client = MongoClient(
                mongodb_uri,
                tls=True,
                tlsCAFile=mongodb_certificate_path,
                serverSelectionTimeoutMS=5000
            )
        
        # Attempt to retrieve the server information
        client.admin.command('ping')
        print("MongoDB is running.")

        return client
    
    except ConnectionFailure as e:
        print(f"❌ MongoDB is not running: {e}")

def get_collection(client, db_name, collection_name):
    # Access the database dynamically
    db = client[db_name]
    # Access the collection dynamically
    collection = db[collection_name]
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

def drop_database(client, db_name):
    """Drop an entire database"""
    client.drop_database(db_name)
    print(f"Database '{db_name}' dropped.")


if __name__ == "__main__":
    client = check_mongodb_status()

    if client:
        collection = get_collection(client, "mongo_db", "mongo_collection")
        print(collection)

        drop_database(client, "mongo_db")

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
