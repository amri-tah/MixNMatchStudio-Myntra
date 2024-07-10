import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client.myntra_database
collection_prod = db.products

products = [
    {
        "name": "Stylish Shirt",
        "price": 29.99,
        "category": "Clothing",
        "stock": 100,
        "description": "A stylish shirt for all occasions.",
        "tags": ["shirt", "stylish", "casual"]
    },
    {
        "name": "Elegant Dress",
        "price": 59.99,
        "category": "Clothing",
        "stock": 50,
        "description": "An elegant dress perfect for evening events.",
        "tags": ["dress", "elegant", "evening"]
    },
    {
        "name": "Running Shoes",
        "price": 49.99,
        "category": "Footwear",
        "stock": 150,
        "description": "Comfortable running shoes for daily use.",
        "tags": ["shoes", "running", "comfort"]
    }
]

result = collection_prod.insert_many(products)
print(f"Products inserted with _ids: {result.inserted_ids}")

for product in collection_prod.find():
    print(product)