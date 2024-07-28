import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import ObjectId

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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/original/coll1_1.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/segmented/coll1_2.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/original/coll1_3.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/original/coll2_1.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/original/coll2_2.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/segmented/coll2_3.png",
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
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/segmented/coll2_4.png",
    },
    {
        "brand": "Sherrif Shoes", 
        "name": "Women Black Solid Heels",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll2_5.png",
        "category": "Accessories",
        "rating": 4.5,
        "no_of_rating": "83",
        "price": 1467,
        "sizes": ["33", "34", "35", "36", "37", "38"],
        "segmented_image_url":  "https://myntra-products.s3.amazonaws.com/segmented/coll2_5.png",
    },
    {
        "brand": "FREAKINS", 
        "name": "Men Blue Mildly Distressed Pure Cotton Jeans",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll7_1.png",
        "category": "Men",
        "rating": 4.1,
        "no_of_rating": "89",
        "price": 1439,
        "sizes": ["28", "30", "32", "34", "36"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/original/coll7_1.png",
    },
    {
        "brand": "Rigo", 
        "name": "Striped Sleeveless Cotton Slim Fit Innerwear Vest SD03241079RL",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll7_2.png",
        "category": "Men",
        "rating": 3.8,
        "no_of_rating": "26",
        "price": 279,
        "sizes": ["S", "M", "L", "XL"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll7_2.png",
    },
    {
        "brand": "Rigo", 
        "name": "Abstract Printed Slim Fit Co-Ords",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll8_1.png",
        "category": "Men",
        "rating": 4.0,
        "no_of_rating": "78",
        "price": 999,
        "sizes": ["S", "M", "L", "XL"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll8_1.png",
    },
    {
        "brand": "Rigo", 
        "name": "Solid Drop-Shoulder Sleeves Oversized Casual Shirt",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll9_1.png",
        "category": "Men",
        "rating": 3.9,
        "no_of_rating": "54",
        "price": 649,
        "sizes": ["S", "M", "L", "XL"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll9_1.png",
    },
    {
        "brand": "HERE&NOW", 
        "name": "Varsity Printed Shorts",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll9_2.png",
        "category": "Men",
        "rating": 4.2,
        "no_of_rating": "42",
        "price": 719,
        "sizes": ["28", "30", "32", "34", "36"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll9_2.png",
    },
    {
        "brand": "The Roadster Life Co.", 
        "name": "Men 90s Redux Slim Tapered Fit Applique Jeans",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll9_3.png",
        "category": "Men",
        "rating": 4.3,
        "no_of_rating": "25",
        "price": 1649,
        "sizes": ["28", "30", "32", "34", "36"],
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll9_3.png",
    },
    {
        "brand": "BAESD",
        "name": "Abstract Printed Halter Neck Crop Regular Top",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll3_1.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll3_1.png",
        "category": "Women",
        "rating": 4.3,
        "no_of_rating": "500",
        "price": 799,
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "brand": "Stylecast X Kotty",
        "name": "Straight Midi Skirts",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll3_2.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll3_2.png",
        "category": "Women",
        "rating": 4.2,
        "no_of_rating": "200",
        "price": 999,
        "sizes": ["26", "28", "30", "32"],
    },
    {
        "brand": "Stylecast X Kotty",
        "name": "Women Straight Fit High-Rise Heavy Fade Stretchable Jeans",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll4_2.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll4_2.png",
        "category": "Women",
        "rating": 4.5,
        "no_of_rating": "150",
        "price": 1199,
        "sizes": ["26", "28", "30", "32", "34"],
    },
    {
        "brand": "Stylecast X Hersheinbox",
        "name": "Printed Drop-Shoulder Sleeves Cotton Relaxed Fit T-shirt",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll4_1.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll4_1.png",
        "category": "Women",
        "rating": 4.0,
        "no_of_rating": "300",
        "price": 599,
        "sizes": ["S", "M", "L", "XL", "XXL"],
    },
    {
        "brand": "Stylecast X Slyck",
        "name": "V-Neck Puff Sleeves Shirt Style Top",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll5_1.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll5_1.png",
        "category": "Women",
        "rating": 4.3,
        "no_of_rating": "180",
        "price": 799,
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "brand": "StyleCast x Revolte",
        "name": "Flared Sleeve Tulip A-Line Dress",
        "img_url": "https://myntra-products.s3.amazonaws.com/original/coll6_1.png",
        "segmented_image_url": "https://myntra-products.s3.amazonaws.com/segmented/coll6_1.png",
        "category": "Women",
        "rating": 4.5,
        "no_of_rating": "250",
        "price": 1499,
        "sizes": ["XS", "S", "M", "L", "XL"],
    },
]


mixnmatch = [
    {
        "name": "Cool Fit",
        "description": "A perfect casual outfit for a day out.",
        "user": "InnovateHers",
        "cover_img": "https://myntra-products.s3.amazonaws.com/original/coll4_1.png",
        "products": [{"id": ObjectId("6693b75e1ab7b3734f561f15"), "x": 50,
      "y": 50,
      "width": 100,
      "height": 100}, {"id":ObjectId("6693b75e1ab7b3734f561f14"), "x": 90,
      "y": 90,
      "width": 100,
      "height": 100}],  
        "likes": 5,
        "saves": 10
    },
    # {
    #     "name": "Elegant Evening",
    #     "description": "An elegant look for evening events.",
    #     "user": "InnovateHers",
    #     "cover_img": "https://myntra-products.s3.amazonaws.com/original/coll2_3.png",
    #     "products": ["6693b75e1ab7b3734f561f07", "6693b75e1ab7b3734f561f08", "6693b75e1ab7b3734f561f09", "6693b75e1ab7b3734f561f0a", "6693b75e1ab7b3734f561f0b"],  
    #     "likes": 8,
    #     "saves": 5
    # },
]

# result = collection_prod.insert_many(products)
result = collection_mixnmatch.insert_many(mixnmatch)
print(f"Products inserted with _ids: {result.inserted_ids}")

for product in collection_mixnmatch.find():
    print(product)