import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

def push_data_to_mongodb(data):
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(mongo_uri)

        # Access the database 
        db = client.payloadDatabase

        # Access the collection
        collection = db["webhook_data"]

        # Insert data into the collection
        result = collection.insert_one(data)
        print("Data inserted successfully. Inserted ID:", result.inserted_id)

    except Exception as e:
        print("Error:", e)

# Example data 
data = {
    'request_id': '123456789',
    'author': 'subhojeet',
    'action': 'PUSH',
    'from_branch': 'my-branch',
    'to_branch': 'main',
    'timestamp': '2022-04-01T10:00:00Z'
}

# Call the function to push data to MongoDB
push_data_to_mongodb(data)
