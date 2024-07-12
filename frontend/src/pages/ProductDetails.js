import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import bag from '../assets/bag.png';

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
      const response = await axios.post('/mixnmatch/', {
        name: newCanvasName,
        description: newCanvasDescription,
        user: "InnovateHers", // Assuming you have a user context or can retrieve it from elsewhere
        cover_img: "https://myntra-products.s3.amazonaws.com/original/coll2_3.png",
        products: [id]
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
    <div className="p-10">
      <h1 className="text-md font-bold mb-4 ml-10">
        <span className="font-normal">Home/{product.category}/ </span>{product.name}
      </h1>
      <div className="flex gap-[100px] ml-10">
        <div><img src={product.img_url} width={400} alt={product.name} /></div>
        <div>
          <h1 className="font-bold text-2xl">{product.brand}</h1>
          <h1 className="font-normal text-lg">{product.name}</h1>
          <h1 className="font-bold text-2xl mt-7">₹ {product.price}</h1>
          <h1 className="font-bold text-md text-green-600">inclusive of all taxes</h1>
          <h1 className="font-normal text-lg mt-5">SELECT SIZE</h1>
          <div className="flex gap-7 text-lg">
            {product.sizes.map((size) => (
              <div key={size} className="flex justify-center items-center p-4 mt-2 mb-10 border-2 border-gray-600">{size}</div>
            ))}
          </div>
          <button className="w-[370px] h-[60px] bg-[#FF3F6C] text-white font-semibold text-lg">ADD TO BAG</button>
          <div className="flex gap-[10px] w-[370px] h-[60px] justify-center items-center border-2 border-[#FF3F6C] text-[#FF3F6C] font-semibold text-lg mt-5 relative">
            <img src={bag} width={20} height={20} alt="Add to MixNMatch" />
            <select
              value={selectedCollection}
              onChange={(e) => setSelectedCollection(e.target.value)}
              className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            >
              <option value="">Add to MixNMatch</option>
              {mixnmatchCollections.map((collection) => (
                <option key={collection._id} value={collection._id}>{collection.name}</option>
              ))}
              <option value="new">Create New Canvas</option>
            </select>
          </div>
          <button
            className="w-[370px] h-[60px] bg-[#FF3F6C] text-white font-semibold text-lg mt-5"
            onClick={handleAddToMixNMatch}
          >
            CONFIRM ADD TO MIXNMATCH
          </button>
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
