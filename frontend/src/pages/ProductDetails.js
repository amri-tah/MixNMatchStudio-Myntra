import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ProductDetails = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        const response = await axios.get(`/products/${id}`);
        setProduct(response.data);
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    };

    fetchProductDetails();
  }, [id]);

  if (!product) return <div>Loading...</div>;

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">{product.name}</h1>
      <p className="mb-2">{product.description}</p>
      <p className="mb-2">Price: {product.price}</p>
      <p className="mb-2">Category: {product.category}</p>
      <p className="mb-2">Stock: {product.stock}</p>
      <p className="mb-2">Tags: {product.tags.join(', ')}</p>
    </div>
  );
};

export default ProductDetails;
