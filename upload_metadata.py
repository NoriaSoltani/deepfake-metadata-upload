import json
from pymongo import MongoClient

# Path to merged JSON dataset
merged_json_path = input("Enter the full path to your merged JSON dataset: ")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["deepfake_M_datasets"]          # database name
collection = db["deepfake_merged_datasets"] # collection name

# INSERT PROCESS
print(f"Loading merged dataset from:\n{merged_json_path}")

# Load JSON file
try:
    with open(merged_json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
    exit(1)

# Insert all documents
result = collection.insert_many(metadata)

print(f"Inserted {len(result.inserted_ids)} documents.")
print("Inserted successfully!")



