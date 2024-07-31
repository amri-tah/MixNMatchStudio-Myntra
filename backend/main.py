import os
from fastapi import FastAPI, HTTPException, Request, Query, Body
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Tuple
from fuzzywuzzy import process
import math
import requests
import random
import logging
import google.generativeai as genai


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
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = MongoClient(uri)
db = client.myntra_database
collection_prod = db.products
collection_mixnmatch = db.mixnmatch
collection_cart = db.cart

# Configure Google Generative AI
genai.configure(api_key=gemini_api_key)

class MixNMatchCreate(BaseModel):
    name: str
    description: str
    user: str
    cover_img: str

class ProductPosition(BaseModel):
    id: str
    x: Optional[float] = 100
    y: Optional[float] = 100
    width: Optional[float] = 100
    height: Optional[float] = 100

def search_products(query: str, products: List[dict], limit: int = 1) -> List[dict]:
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

def get_keywords_from_gemini(query: str) -> Tuple[List[str], str]:
    genai.configure(api_key=gemini_api_key)
    
    # Prompt to generate keywords
    keywords_prompt = f'''
    You are a fashion expert. Given a customer's situation, generate five keywords related to suitable clothing options for them. For example, if the customer's query is "I want to go to a business conference," the keywords could be "blazer, suit, formal dress." Customer query: "{query}" Keywords:
    '''
    
    # Prompt to provide chatbot-like suggestions
    suggestions_prompt = f'''
    You are a fashion expert. Based on the customer's query, provide some outfit suggestions that could be suitable for their situation. Keep the suggestions short and sweet. Max 2 sentances. For example, if the customer's query is "I want to go to a business conference," you might suggest "a tailored suit, a formal dress, or a blazer with trousers." Customer query: "{query}" Suggestions:
    '''
    
    # Generate content using the configured model
    model = genai.GenerativeModel('gemini-1.5-flash')
    keywords_response = model.generate_content([keywords_prompt])
    suggestions_response = model.generate_content([suggestions_prompt])
    
    # Extract the keywords and suggestions from the responses
    keywords = keywords_response.text.strip().split(", ")
    suggestions = suggestions_response.text.strip()
    
    return keywords, suggestions

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

@app.get("/aisearch")
async def ai_search(query: Optional[str] = Query(None)):
    try:
        # Print the initial query
        print(f"Received query: {query}")
        
        products_cursor = collection_prod.find()
        products = [product_helper(product) for product in products_cursor]
        
        # Print the total number of products found
        print(f"Total products found: {len(products)}")
        
        if query:
            # Print before calling the Gemini API
            print("Calling Gemini API to get keywords...")
            keywords, suggestions = get_keywords_from_gemini(query)
            
            # Print the received keywords
            print(f"Keywords received: {keywords}")
            
            matched_products = []
            for keyword in keywords:
                matched_products.extend(search_products(keyword, products))
                
                # Print matched products for each keyword
                print(f"Matched products for keyword '{keyword}': {matched_products}")
            
            # Remove duplicates while preserving order
            seen = set()
            products = [p for p in matched_products if p["id"] not in seen and not seen.add(p["id"])]
            
            # Print the final matched products after removing duplicates
            print(f"Final matched products: {products}")
            
            return {"keywords": keywords, "suggestions":suggestions, "products": products}
        
        return {"query": products}
    except Exception as e:
        # Print the exception if any occurs
        print(f"Error: {str(e)}")
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

@app.put("/mixnmatch/{collection_id}/add_product/{product_id}")
async def add_product_to_collection(collection_id: str, product_id: str):
    try:
        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        product_doc = collection_prod.find_one({"_id": ObjectId(product_id)})
        if not product_doc:
            raise HTTPException(status_code=404, detail="Product not found")

        collection_mixnmatch.update_one(
            {"_id": ObjectId(collection_id)},
            {"$addToSet": {"products": {"id": ObjectId(product_id), "x": 100, "y": 100, "width": 100, "height": 100}}}
        )

        return {"message": "Product added to collection successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/mixnmatch/{collection_id}/remove_product/{product_id}")
async def remove_product_from_collection(collection_id: str, product_id: str):
    try:
        if not ObjectId.is_valid(collection_id):
            raise HTTPException(status_code=400, detail="Invalid collection_id")
        if not ObjectId.is_valid(product_id):
            raise HTTPException(status_code=400, detail="Invalid product_id")
        
        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        collection_mixnmatch.update_one(
            {"_id": ObjectId(collection_id)},
            {"$pull": {"products": {"id": ObjectId(product_id)}}}
        )

        return {"message": "Product removed from collection successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/mixnmatch/{product_id}")
async def create_mixnmatch_collection(product_id: str, collection: MixNMatchCreate):
    try:
        if not ObjectId.is_valid(product_id):
            raise HTTPException(status_code=400, detail="Invalid product_id")
        
        product_doc = collection_prod.find_one({"_id": ObjectId(product_id)})
        if not product_doc:
            raise HTTPException(status_code=404, detail="Product not found")

        new_collection = {
            "name": collection.name,
            "description": collection.description,
            "user": collection.user,
            "cover_img": collection.cover_img,
            "likes": 0,
            "saves": 0,
            "products": [{"id": ObjectId(product_id), "x": 100, "y": 100, "width": 100, "height": 100}]
        }
        result = collection_mixnmatch.insert_one(new_collection)
        created_collection = collection_mixnmatch.find_one({"_id": result.inserted_id})
        return mixnmatch_helper(created_collection)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@app.put("/mixnmatch/{collection_id}/save_positions/")
async def save_positions(collection_id: str, products: List[ProductPosition]):
    try:
        if not ObjectId.is_valid(collection_id):
            raise HTTPException(status_code=400, detail="Invalid collection_id")

        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        updated_products = [
            {"id": ObjectId(product.id), "x": int(product.x), "y": int(product.y), "width": int(product.width), "height": int(product.height)}
            for product in products
        ]

        collection_mixnmatch.update_one(
            {"_id": ObjectId(collection_id)},
            {"$set": {"products": updated_products}}
        )

        return {"message": "Positions and sizes updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/cart/{user_id}/{collection_id}")
async def add_collection_to_cart(collection_id: str, user_id: str):
    try:
        if not ObjectId.is_valid(collection_id):
            raise HTTPException(status_code=400, detail="Invalid collection_id")

        collection = collection_mixnmatch.find_one({"_id": ObjectId(collection_id)})
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")

        product_ids = [ObjectId(prod["id"]) for prod in collection["products"]]
        products = collection_prod.find({"_id": {"$in": product_ids}})
        cart_items = [product_helper(product) for product in products]

        for item in cart_items:
            collection_cart.update_one(
                {"user_id": user_id},
                {"$addToSet": {"items": item}},
                upsert=True
            )

        return {"message": "Products from collection added to cart successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cart/{user_id}")
async def get_cart(user_id: str):
    try:
        cart = collection_cart.find_one({"user_id": user_id})
        if not cart:
            return {"items": []}
        return {"items": cart.get("items", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
