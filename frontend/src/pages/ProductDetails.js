import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import bag from '../assets/bag.png'
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
      <h1 className="text-md font-bold mb-4 ml-10"><span className='font-normal'>Home/{product.category}/ </span>{product.name}</h1>
      <div className=' flex gap-[100px] ml-10'>
      <div><img src={product.img_url} width={400} alt={product.name}/></div>
      
      <div>
        <h1 className='font-bold text-2xl'>{product.brand}</h1>
        <h1 className='font-normal text-lg'>{product.name}</h1>
        <h1 className='font-bold text-2xl mt-7'>₹ {product.price}</h1>
        <h1 className='font-bold text-md text-green-600'>inclusive of all taxes</h1>

        <h1 className='font-normal text-lg mt-5'>SELECT SIZE</h1>
        <div className='flex gap-7 text-lg'>
          {product.sizes.map((size) => (
            <div className='flex items-center justify-center p-4 bg-white rounded-full border border-pink-500'>
            {size}
          </div>
          )

          )}
          </div>

          <div className='bg-pink-500 px-5 py-4 text-white text-md w-fit my-4 rounded-lg flex justify-center items-center mt-5'>
            <div>
            <img src={bag} width={25} height={25} alt="bag" />
            </div>
            <div>ADD TO CART</div>
            
            </div>
            <div className='bg-white px-5 py-4 text-md w-fit my-4 rounded-xl border-2 border-black'>
            <div>Add to MixNMatch Studio</div></div>

            
      </div>
      </div>
      
    </div>
  );
};

export default ProductDetails;
