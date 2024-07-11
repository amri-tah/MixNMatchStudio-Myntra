import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CatalogCard from '../components/CatalogCard';
import { Link } from 'react-router-dom';

const Catalog = ({ prod_type }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('/products/');
        const filteredProducts = response.data.filter(product => product.category === prod_type);
        setProducts(filteredProducts);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, [prod_type]);

  return (
    <div className="p-10">
      <h1 className="text-xl font-bold mb-4">Home/{prod_type}</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {products.map((product) => (
          <Link key={product.id} to={`/product/${product.id}`} className="flex justify-center">
            <CatalogCard key={product.id} name={product.name} />
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Catalog;
