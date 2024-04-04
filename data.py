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
        request_id = payload.get('head_commit').get('id')  # Use commit ID from head_commit
        author = payload.get('head_commit').get('author').get('name')  # Get author name from head_commit
        action = "PUSH"  # Assuming this is always a push event based on the provided payload
        from_branch = payload.get('base_ref')  # Use base_ref as from_branch
        to_branch = payload.get('ref')  # Use ref as to_branch
        timestamp = datetime.strptime(payload.get('head_commit').get('timestamp'), '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')  # Get timestamp from head_commit and convert to desired format

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
