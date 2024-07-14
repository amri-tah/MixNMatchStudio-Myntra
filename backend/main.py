import os
from fastapi import FastAPI, HTTPException, Request
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from bson.json_util import dumps, loads
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
collection_mixnmatch = db.mixnmatch

class MixNMatchCreate(BaseModel):
    name: str
    description: str
    user: str
    cover_img: str


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
        "products": [str(prod_id) for prod_id in collection["products"]]
    }

@app.get("/")
async def hello_world():
    return {"Team":"InnovateHers", "Members": ["Amritha Nandini", "Dharsini Sri", "Shruti Sivakumar"], "Institute": "Amrita Vishwa Vidyapeetham, Coimbatore"}

@app.get("/products/")
async def get_products():
    try:
        products_cursor = collection_prod.find()
        products = [product_helper(product) for product in products_cursor]
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
            product_ids = collection["products"]
            products = [product_helper(collection_prod.find_one({"_id": ObjectId(pid)})) for pid in product_ids]
            collection_details["products"] = products
            return collection_details
        else:
            raise HTTPException(status_code=404, detail="Collection not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/mixnmatch/{collection_id}/add_product/{product_id}")
async def add_product_to_collection(collection_id: str, product_id: str):
    try:
        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        product = collection_prod.find_one({"_id": ObjectId(product_id)})
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        collection_mixnmatch.update_one(
            {"_id": ObjectId(collection_id)},
            {"$addToSet": {"products": ObjectId(product_id)}}
        )

        return {"message": "Product added to collection successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/mixnmatch/{product_id}")
async def create_mixnmatch_collection(product_id: str, collection: MixNMatchCreate):
    try:
        new_collection = {
            "name": collection.name,
            "description": collection.description,
            "user": collection.user,
            "cover_img": collection.cover_img,
            "likes": 0,
            "saves": 0,
            "products": [ObjectId(product_id)]
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