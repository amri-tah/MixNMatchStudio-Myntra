import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import bag from '../assets/bag.png';
import heart from '../assets/Heart.png'
import star from '../assets/star.png'

const ProductDetails = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [mixnmatchCollections, setMixnmatchCollections] = useState([]);
  const [selectedCollection, setSelectedCollection] = useState('');
  const [showDialog, setShowDialog] = useState(false);
  const [newCanvasName, setNewCanvasName] = useState('');
  const [newCanvasDescription, setNewCanvasDescription] = useState('');

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        const response = await axios.get(`/products/${id}`);
        setProduct(response.data);
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    };

    const fetchMixnmatchCollections = async () => {
      try {
        const response = await axios.get('/mixnmatch/');
        setMixnmatchCollections(response.data);
      } catch (error) {
        console.error('Error fetching MixNMatch collections:', error);
      }
    };

    fetchProductDetails();
    fetchMixnmatchCollections();
  }, [id]);

  const handleAddToMixNMatch = async () => {
    if (selectedCollection === 'new') {
      setShowDialog(true);
    } else if (selectedCollection) {
      try {
        const collection = mixnmatchCollections.find(coll => coll.name === selectedCollection);
        if (collection) {
          await axios.put(`/mixnmatch/${collection.id}/add_product/${id}`, {
            product_id: id
          });
          alert('Product added to existing collection');
        } else {
          console.error('Selected collection not found');
        }
      } catch (error) {
        console.error('Error adding product to collection:', error);
      }
    } else {
      console.error('No collection selected');
    }
  };

  const handleCreateNewCanvas = async () => {
    try {
        const response = await axios.post(`/mixnmatch/${product.id}`, {
            name: newCanvasName,
            description: newCanvasDescription,
            user: "InnovateHers",
            cover_img: product.img_url,
        });
        setShowDialog(false);
        setMixnmatchCollections([...mixnmatchCollections, response.data]);
        alert('New canvas created and product added');
    } catch (error) {
        console.error('Error creating new canvas:', error);
    }
};

  if (!product) return <div>Loading...</div>;

  return (
    <div className="p-10 mb-7">
      <h1 className="text-md font-bold mb-4 ml-10">
        <span className="font-normal">Home/{product.category}/ </span>{product.name}
      </h1>
      <div className="flex gap-[100px] ml-10">
        <div><img src={product.img_url} width={400} alt={product.name} /></div>
        <div>
          <h1 className="font-bold text-2xl">{product.brand}</h1> 
          <h1 className="font-normal text-lg">{product.name}</h1>
          <div className='flex border gap-2 w-fit p-2'>
            <div className='flex gap-2 items-center'>
              {product.rating}
              <img src={star} width={20} alt='rating'/>
              </div> | {product.norating} Ratings
          </div>
          <h1 className="font-bold text-[2rem] mt-7">₹ {product.price}</h1>
          <h1 className="text-md text-green-600">inclusive of all taxes</h1>
          <h1 className="font-normal text-lg mt-5">SELECT SIZE</h1>
          <div className="flex gap-7 text-lg">
            {product.sizes.map((size) => (
              <div key={size} className="flex justify-center items-center  px-4 py-2 mt-2 mb-10 border-2 rounded-2xl border-[#FF3F6C]">{size}</div>
            ))}
          </div>
          <div className='flex items-center gap-5'>
          <button className=" bg-[#FF3F6C] text-white font-semibold text-lg px-5 py-3 rounded-lg flex items-center gap-3">
          <img src={bag} width={20} height={20} alt="Add to MixNMatch" />
          ADD TO BAG</button>
          <img src={heart} width={30} alt='heart'></img>
          </div>
          
          <div className="flex gap-4 justify-center items-center mt-4 ">
            <div className='border-2 border-[#FF3F6C] text-md text-[#FF3F6C] font-semibold  px-5 py-3'>
            <select
              value={selectedCollection}
              onChange={(e) => setSelectedCollection(e.target.value)}
              className="w-full h-full cursor-pointer text-md text-black focus:outline-none"
            >
              <option value="" disabled selected className='text-black '>Add to Mix&Match Studio</option>
              <option value="new">Create New Canvas</option>
              {mixnmatchCollections.map((collection) => (
                <option key={collection._id} value={collection._id}>{collection.name}</option>
              ))}
            </select>

            </div>
            <button
            className="px-5 py-3 rounded-lg flex items-center gap-3 bg-[#FF3F6C] text-white font-semibold text-lg"
            onClick={handleAddToMixNMatch}
          >
            Add to Mix&Match Studio
          </button>
          </div>
          
        </div>
      </div>
      {showDialog && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
          <div className="bg-white p-6 rounded shadow-lg">
            <h2 className="text-lg font-bold mb-4">Create New Canvas</h2>
            <label className="block mb-2">
              Canvas Name:
              <input
                type="text"
                className="block w-full border rounded py-2 px-3"
                value={newCanvasName}
                onChange={(e) => setNewCanvasName(e.target.value)}
              />
            </label>
            <label className="block mb-2">
              Description:
              <textarea
                className="block w-full border rounded py-2 px-3"
                value={newCanvasDescription}
                onChange={(e) => setNewCanvasDescription(e.target.value)}
              />
            </label>
            <div className="flex justify-end mt-4">
              <button
                className="bg-blue-500 text-white px-4 py-2 rounded mr-2"
                onClick={handleCreateNewCanvas}
              >
                Create
              </button>
              <button
                className="bg-gray-500 text-white px-4 py-2 rounded"
                onClick={() => setShowDialog(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProductDetails;
