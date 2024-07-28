import os
from fastapi import FastAPI, HTTPException, Request, Query, Body
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from fuzzywuzzy import process

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client.myntra_database
collection_prod = db.products
collection_mixnmatch = db.mixnmatch

class MixNMatchCreate(BaseModel):
    name: str
    description: str
    user: str
    cover_img: str

class ProductPosition(BaseModel):
    id: str
    x: int
    y: int
    width: int
    height: int

def search_products(query: str, products: List[dict], limit: int = 4) -> List[dict]:
    product_names = [product["name"] for product in products]
    results = process.extract(query, product_names, limit=limit)
    matched_products = [products[product_names.index(result[0])] for result in results]
    return matched_products

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "brand": product["brand"],
        "name": product["name"],
        "img_url": product["img_url"],
        "seg_url": product["segmented_image_url"],
        "price": product["price"],
        "category": product["category"],
        "rating": product["rating"],
        "norating": product["no_of_rating"],
        "sizes": product["sizes"]
    }

def mixnmatch_helper(collection) -> dict:
    return {
        "id": str(collection["_id"]),
        "user": collection.get("user", "Anonymous"),
        "name": collection["name"],
        "img_url": collection["cover_img"],
        "likes": collection["likes"],
        "saves": collection["saves"],
        "products": [
            {
                "id": str(prod["id"]),
                "x": prod["x"],
                "y": prod["y"],
                "width": prod["width"],
                "height": prod["height"]
            }
            for prod in collection["products"]
        ]
    }

@app.get("/")
async def hello_world():
    return {"Team":"InnovateHers", "Members": ["Amritha Nandini", "Dharsini Sri", "Shruti Sivakumar"], "Institute": "Amrita Vishwa Vidyapeetham, Coimbatore"}

@app.get("/products/")
async def get_products(query: Optional[str] = Query(None)):
    try:
        products_cursor = collection_prod.find()
        products = [product_helper(product) for product in products_cursor]

        if query:
            products = search_products(query, products)
        
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products/{product_id}")
async def get_product_by_id(product_id: str):
    try:
        product = collection_prod.find_one({"_id": ObjectId(product_id)})
        if product:
            return product_helper(product)
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/mixnmatch/")
async def get_collections():
    try:
        collection_cursor = collection_mixnmatch.find()
        collections = [mixnmatch_helper(collection) for collection in collection_cursor]
        return collections
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/mixnmatch/{collection_id}")
async def get_collection_by_id(collection_id: str):
    try:
        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if collection:
            collection_details = mixnmatch_helper(collection)
            products = [
                {
                    **product_helper(collection_prod.find_one({"_id": ObjectId(prod["id"])})),
                    "x": prod["x"],
                    "y": prod["y"],
                    "width": prod["width"],
                    "height": prod["height"]
                }
                for prod in collection["products"]
            ]
            collection_details["products"] = products
            return collection_details
        else:
            raise HTTPException(status_code=404, detail="Collection not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/mixnmatch/{collection_id}/add_product/")
async def add_product_to_collection(collection_id: str, product: ProductPosition):
    try:
        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        product_doc = collection_prod.find_one({"_id": ObjectId(product.id)})
        if not product_doc:
            raise HTTPException(status_code=404, detail="Product not found")

        collection_mixnmatch.update_one(
            {"_id": ObjectId(collection_id)},
            {"$addToSet": {"products": {"id": ObjectId(product.id), "x": product.x, "y": product.y, "width": product.width, "height": product.height}}}
        )

        return {"message": "Product added to collection successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/mixnmatch/{product_id}")
async def create_mixnmatch_collection(product_id: str, collection: MixNMatchCreate, product: ProductPosition):
    try:
        new_collection = {
            "name": collection.name,
            "description": collection.description,
            "user": collection.user,
            "cover_img": collection.cover_img,
            "likes": 0,
            "saves": 0,
            "products": [{"id": ObjectId(product.id), "x": product.x, "y": product.y, "width": product.width, "height": product.height}]
        }
        result = collection_mixnmatch.insert_one(new_collection)
        created_collection = collection_mixnmatch.find_one({"_id": result.inserted_id})
        return mixnmatch_helper(created_collection)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
