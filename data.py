import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
# Access the database 
db = client.payloadDatabase
# Access the collection
collection = db["webhook_data"]

def push_data_to_mongodb(payload):
    try:
        # Extracting required fields from the webhook payload
        request_id = payload.get('commit_id') if payload.get('commit_id') else payload.get('pr_id')
        author = payload.get('author')
        action = payload.get('action')
        from_branch = payload.get('from_branch')
        to_branch = payload.get('to_branch')
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp in UTC
        
        # Store payload in MongoDB
        data = {
            'request_id': request_id,
            'author': author,
            'action': action,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp
        }

        # Insert data into the collection
        result = collection.insert_one(data)
        print("Data inserted successfully. Inserted ID:", result.inserted_id)

    except Exception as e:
        print("Error:", e)
