from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client["experiments"]
collection = db["experiment_data"]

@app.route('/api/data', methods=['POST'])
def insert_data():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully"}), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
