from flask import Blueprint, request, jsonify
from data import push_data_to_mongodb

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():

    payload = request.json  # Extract JSON payload from GitHub webhook
    push_data_to_mongodb(payload)

    return jsonify({"message": "Webhook data stored successfully"}), 200
