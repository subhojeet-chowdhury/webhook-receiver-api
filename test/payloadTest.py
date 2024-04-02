import requests
import json

# Define the URL of your webhook endpoint
webhook_url = 'https://webhook-api-d7a115650405.herokuapp.com/webhook/receiver'  # Update with your actual webhook URL

# Example payload data
payload_data = {
    'commit_id': '123456789',
    'author': 'herokuuu',
    'action': 'PUSH',
    'from_branch': 'payload-api-test',
    'to_branch': 'main',
    'timestamp': '2022-04-01T10:00:00Z'
}

# Convert payload data to JSON format
payload_json = json.dumps(payload_data)

# Send POST request with payload data to webhook endpoint
response = requests.post(webhook_url, data=payload_json, headers={'Content-Type': 'application/json'})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Payload sent successfully!")
else:
    print("Failed to send payload. Status code:", response.status_code, response)
