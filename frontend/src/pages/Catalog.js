import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CatalogCard from '../components/CatalogCard';
import { Link, useLocation } from 'react-router-dom';

const Catalog = ({ prod_type }) => {
  const [products, setProducts] = useState([]);
  const location = useLocation();
  const searchQuery = new URLSearchParams(location.search).get('query');

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('/products/', { params: { query: searchQuery } });
        console.log('Response data:', response.data);
        let filteredProducts = response.data;

        if (prod_type) {
          filteredProducts = filteredProducts.filter(product => product.category === prod_type);
        }

        setProducts(filteredProducts);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, [prod_type, searchQuery]);

  return (
    <div className="p-10">
      <h1 className="text-xl font-bold mb-4 ml-10">
        <span className='font-normal'>Home/ </span>
        {prod_type || 'Search Results'}
      </h1>
      <div className="grid grid-cols-4 sm:grid-cols-2 lg:grid-cols-4 gap-2">
        {products.map((product) => (
          <Link key={product.id} to={`/product/${product.id}`} className="flex justify-center">
            <CatalogCard key={product.id} name={product.name} img_url={product.img_url} brand={product.brand} price={product.price} />
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Catalog;
