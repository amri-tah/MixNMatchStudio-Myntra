import React from 'react';

const CatalogCard = ({ brand, name, img_url, price }) => {
  return (
    <div className="bg-white p-6 flex flex-col justify-between max-w-[300px] rounded-lg shadow-xl">
      <div className="overflow-hidden bg-gray-200 w-full aspect-w-4 aspect-h-3">
        <img
          src={img_url}
          alt={name}
          className="object-cover w-full h-full"
        />
      </div>
      <div className="mt-4">
        <h2 className="text-sm font-bold leading-5">{brand}</h2>
        <h2 className="text-sm font-normal leading-5">{name}</h2>
        <h2 className="mt-2 text-md font-bold leading-5">Rs {price}</h2>
      </div>
    </div>
  );
};

export default CatalogCard;
