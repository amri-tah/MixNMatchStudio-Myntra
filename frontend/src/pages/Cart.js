// src/components/Cart.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    const fetchCartItems = async () => {
      try {
        const user_id = 'InnovateHers'; 
        const response = await axios.get(`/cart/${user_id}`);
        setCartItems(response.data.items);
      } catch (error) {
        console.error('Error fetching cart items:', error);
      }
    };

    fetchCartItems();
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Your Cart</h2>
      {cartItems.length === 0 ? (
        <p className="text-lg text-gray-600">Your cart is empty.</p>
      ) : (
        <div className="space-y-4">
          {cartItems.map((item) => (
            <div key={item.id} className="flex items-center border border-gray-200 rounded-lg p-4 shadow-md">
              <img src={item.img_url} alt={item.name} className="w-32 h-32 object-cover rounded-md mr-4" />
              <div className="flex-1">
                <h3 className="text-lg font-semibold">{item.name}</h3>
                <p className="text-gray-500">{item.brand}</p>
                <p className="text-xl font-bold mt-2">${item.price}</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Cart;
