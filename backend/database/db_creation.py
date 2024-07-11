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
collection_mixnmatch = db.mixnmatch
collection_competitions = db.competitions
collection_submissions = db.submissions

products = [
    {
        "brand": "GARDIN", 
        "name": "Women Black Solid Boots",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll1_1.png",
        "category": "Accessories",
        "rating": 4.4,
        "no_of_rating": "502",
        "price": 1599,
        "sizes": ["3", "4", "5", "6", "7", "8"],
    },
    {
        "brand": "Zastraa", 
        "name": "Women Off White Mini-Length Skorts",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll1_2.png",
        "category": "Women",
        "rating": 4.3,
        "no_of_rating": "1.6k",
        "price": 749,
        "sizes": ["26", "28", "30", "32", "34"],
    },
    {
        "brand": "all about you", 
        "name": "Women Brown Cable Knit Pullover",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll1_3.png",
        "category": "Women",
        "rating": 4.2,
        "no_of_rating": "258",
        "price": 899,
        "sizes": ["XL"],
    },
    {
        "brand": "Voyage", 
        "name": "Women Teal & Gold-Toned Cateye Sunglasses With UV Protected Lens",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_1.png",
        "category": "Accessories",
        "rating": 4.4,
        "no_of_rating": "2.6k",
        "price": 756,
        "sizes": ["Onesize"],
    },
    {
        "brand": "Fastrack", 
        "name": "Women Blue Analogue Watch 6222SM02",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_2.png",
        "category": "Accessories",
        "rating": 4.6,
        "no_of_rating": "977",
        "price": 1795,
        "sizes": ["Onesize"],
    },
    {
        "brand": "Tokyo Talkies", 
        "name": "Blue Self Designed Shirt Collar Puff Sleeves Crop Shirt Style Top",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_3.png",
        "category": "Women",
        "rating": 4.6,
        "no_of_rating": "70",
        "price": 447,
        "sizes": ["XS", "S", "M", "L", "XL"],
    },
    {
        "brand": "DressBerry", 
        "name": "Women Relaxed Flared High-Rise Easy Wash Trouser",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_4.png",
        "category": "Women",
        "rating": 3.3,
        "no_of_rating": "21",
        "price": 562,
        "sizes": ["26", "28", "30", "32", "34"],
    },
    {
        "brand": "Sherrif Shoes", 
        "name": "Women Black Solid Heels",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_5.png",
        "category": "Women",
        "rating": 4.5,
        "no_of_rating": "83",
        "price": 1467,
        "sizes": ["33", "34", "35", "36", "37", "38"],
    },
]


mixnmatch = [
    {
        "name": "Casual Day Out",
        "description": "A perfect casual outfit for a day out.",
        "user": "InnovateHers",
        "cover_img": "https://myntra-products.s3.amazonaws.com/original/coll1_3.png",
        "products": ["668ffcf57f80c7b008e0bac4", "668ffcf57f80c7b008e0bac5", "668ffcf57f80c7b008e0bac6"],  
        "likes": 5
    },
    {
        "name": "Elegant Evening",
        "description": "An elegant look for evening events.",
        "user": "InnovateHers",
        "cover_img": "https://myntra-products.s3.amazonaws.com/original/coll2_3.png",
        "products": ["668ffcf57f80c7b008e0bac7", "668ffcf57f80c7b008e0bac8", "668ffcf57f80c7b008e0bac9", "668ffcf57f80c7b008e0baca", "668ffcf57f80c7b008e0bacb"],  
        "likes": 8
    }
]

# result = collection_prod.insert_many(products)
result = collection_mixnmatch.insert_many(mixnmatch)
print(f"Products inserted with _ids: {result.inserted_ids}")

for product in collection_mixnmatch.find():
    print(product)