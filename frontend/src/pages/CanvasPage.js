import React, { useEffect, useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { Stage, Layer } from "react-konva";
import ProductImage from "../components/ProductImage";
import save from "../assets/Add.png";
import add from "../assets/Add1.png";
import remove from "../assets/Remove.png";
import heart from "../assets/Heart.png";

const CanvasPage = () => {
  const { id } = useParams();
  const [copied, setCopied] = useState(false);
  const [collection, setCollection] = useState(null);
  const [images, setImages] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [showDialog, setShowDialog] = useState(false);
  const stageRef = useRef(null);

  useEffect(() => {
    const fetchCollectionDetails = async () => {
      try {
        const response = await axios.get(`/mixnmatch/${id}`);
        const data = response.data;
        setCollection(data);

        const initialImages = data.products.map((product, index) => ({
          id: product.id,
          src: product.seg_url,
          // x: 50 * index,
          // y: 50 * index,
          x: product.x,
          y: product.y,
          width: product.width,
          height: product.height,
        }));
        setImages(initialImages);
      } catch (error) {
        console.error("Error fetching collection details:", error);
      }
    };
    fetchCollectionDetails();
  }, [id]);

  const handleDragEnd = (e, id) => {
    const updatedImages = images.map((image) => {
      if (image.id === id) {
        return {
          ...image,
          x: e.target.x(),
          y: e.target.y(),
        };
      }
      return image;
    });
    setImages(updatedImages);
  };

  const handleTransformEnd = (id, newAttrs) => {
    const updatedImages = images.map((image) => {
      if (image.id === id) {
        return {
          ...image,
          ...newAttrs,
        };
      }
      return image;
    });
    setImages(updatedImages);
  };

  const handleRemoveImage = (id) => {
    const updatedImages = images.filter((image) => image.id !== id);
    setImages(updatedImages);
  };

  const handleAddImage = (product) => {
    const newImage = {
      id: product.id,
      src: product.seg_url,
      x: Math.random() * stageRef.current.width(),
      y: Math.random() * stageRef.current.height(),
      width: 100,
      height: 100,
    };
    setImages([...images, newImage]);
  };

  const handleSave = () => {
    axios
      .put(`/mixnmatch/${collection.id}/save_positions/`, images)
      .then(() => {
        alert("Positions and sizes saved successfully!");
      })
      .catch((error) => {
        console.error("Error saving positions and sizes:", error);
      });
  };

  function copy() {
    const el = document.createElement("input");
    el.value = window.location.href;
    document.body.appendChild(el);
    el.select();
    document.execCommand("copy");
    document.body.removeChild(el);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  const totalPrice = collection
    ? collection.products.reduce((sum, product) => sum + product.price, 0)
    : 0;

  if (!collection) return <div>Loading...</div>;

  return (
    <div className="p-10 ml-[3%]">
      <h1 className="font-normal text-md">
        Home / Mix N Match Studio / {collection.name}
      </h1>
      <div className="flex gap-10">
        <div className="w-[40%] py-5">
          <h1 className="font-bold text-2xl">{collection.name}</h1>
          <div className="w-full h-[500px] rounded-xl mt-2 border-2 p-5 border-black">
            <Stage width={500} height={500} ref={stageRef}>
              <Layer>
                {images.map((image) => (
                  <ProductImage
                    key={image.id}
                    image={image}
                    isSelected={image.id === selectedId}
                    onSelect={(id) => setSelectedId(id)}
                    onDragEnd={handleDragEnd}
                    onTransformEnd={handleTransformEnd}
                  />
                ))}
              </Layer>
            </Stage>
          </div>
          <div className="mt-2 rounded-l flex items-center justify-end gap-2">
            <h3 className="font-bold text-xl"></h3>
            <button
              onClick={() => setShowDialog(true)}
              className="text-lg px-4 py-3 border-2 border-black text-black rounded-xl"
            >
              AI Search
            </button>
            <p className="text-lg px-4 py-3 bg-gradient-to-r from-[#E588B8]  to-[#FF8F2B] text-white rounded-xl">
              Visualize using AI
            </p>
          </div>
        </div>
        <div className="w-[60%] ">
          <h2 className="font-bold text-xl mb-4">
            Products in this Collection:
          </h2>

          <div className="max-h-[500px] h-fit overflow-auto">
            {collection.products.map((product) => (
              <div
                key={product.id}
                className="p-2 rounded-l flex items-center justify-between gap-5"
              >
                <div className="flex items-center gap-5">
                  <img
                    src={product.img_url}
                    alt={product.name}
                    className="w-20 h-20 object-cover rounded-lg"
                  />
                  <div className="flex flex-col">
                    <p className="font-bold">{product.brand}</p>
                    <h3 className="text-lg text-gray-600">{product.name}</h3>
                    <div className="flex mt-1">
                      <button
                        className="px-2 py-1 text-white"
                        onClick={() => handleAddImage(product)}
                      >
                        <img src={add} alt="Add" width={25} />
                      </button>
                      <button
                        className="px-2 py-1 text-white"
                        onClick={() => handleRemoveImage(product.id)}
                      >
                        <img src={remove} alt="Remove" width={25} />
                      </button>
                    </div>
                  </div>
                </div>
                <p className="font-bold text-lg">Rs. {product.price}</p>
              </div>
            ))}
          </div>
          <hr className="border-1 bg-black" />
          <div className="mt-4 p-2 rounded-l flex items-center justify-between gap-5">
            <div className="flex gap-3">
              <button
                onClick={handleSave}
                className="text-lg px-6 py-3 bg-[#CFCFCF] text-black rounded-lg"
              >
                SAVE
              </button>
              <button className={`text-lg px-6 py-3 rounded-lg ${copied ? "bg-green-500 text-white" : "bg-black text-white"}`} onClick={copy}>{!copied ? "Copy link" : "Copied!"}</button>
            </div>

            <p className="font-bold text-2xl">Rs. {totalPrice}</p>
          </div>

          <div className="mt-2 rounded-l flex items-center justify-between gap-5 ">
            <h3 className="font-bold text-xl w-[65%]"></h3>
            <div className="flex gap-2">
              <div>
                <img src={heart} width={32} />
                <h1 className="text-center">{collection.likes}</h1>
              </div>

              <div>
                <img src={save} width={32} />
                <h1 className="text-center">{collection.saves}</h1>
              </div>
            </div>

            <button className="w-fit px-5 py-3 rounded-lg bg-[#FF3F6C] text-white font-semibold text-lg">
              ADD TO BAG
            </button>
          </div>
        </div>
      </div>

      {showDialog && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
          <div className="w-[45%] bg-white flex-row px-10 py-6 rounded-xl">
            <p className="font-bold text-[2rem]">AI Search</p>
            <form className="flex items-center mr-5 border rounded-l-md mb-4">
              <input
                type="text"
                placeholder="Search for products and brands.."
                className=" px-4 py-3 w-full outline-none"
              />
              <button
                type="submit"
                className="bg-[#FF3F6C] text-white px-4 py-3 rounded-md"
              >
                Search
              </button>
            </form>
            <button
              className="bg-gray-500 text-white px-4 py-2 rounded"
              onClick={() => setShowDialog(false)}
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default CanvasPage;
