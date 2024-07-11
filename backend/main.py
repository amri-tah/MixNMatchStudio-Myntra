import os
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from bson.json_util import dumps, loads
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client.myntra_database
collection_prod = db.products

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "stock": product["stock"],
        "description": product["description"],
        "tags": product["tags"]
    }

@app.get("/")
async def hello_world():
    return {"Hello":"World"}

@app.get("/products/")
async def get_products():
    try:
        products_cursor = collection_prod.find()
        products = [product_helper(product) for product in products_cursor]
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
