import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CatalogCard from '../components/CatalogCard';
import { Link } from 'react-router-dom';

const initialProducts = [
  {
    "id": "668ea526b269db9dc9d83e30",
    "name": "Elegant Dress",
    "price": 59.99,
    "category": "Clothing",
    "stock": 50,
    "description": "An elegant dress perfect for evening events.",
    "tags": [
      "dress",
      "elegant",
      "evening"
    ]
  },
  {
    "id": "668ea526b269db9dc9d83e31",
    "name": "Running Shoes",
    "price": 49.99,
    "category": "Footwear",
    "stock": 150,
    "description": "Comfortable running shoes for daily use.",
    "tags": [
      "shoes",
      "running",
      "comfort"
    ]
  },
  {
    "id": "668ea526b269db9dc9d83e2f",
    "name": "Stylish Shirt",
    "price": 29.99,
    "category": "Clothing",
    "stock": 100,
    "description": "A stylish shirt for all occasions.",
    "tags": [
      "shirt",
      "stylish",
      "casual"
    ]
  }
];

const Catalog = () => {
  const [products, setProducts] = useState(initialProducts);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('/products/');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h1>Catalog</h1>
      <div className='flex justify-around'>
        {products.map((product) => (
          <Link key={product.id} to={`/product/${product.id}`}>
            <CatalogCard key={product.id} name={product.name} />
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Catalog;
