import React from "react";
import heart from "../assets/Heart.png";
import save from "../assets/Add.png";

const MixNMatchCard = ({ name, img_url, user, likes, saves }) => {
  return (
    <div>
      <div className="bg-white p-6 flex flex-col justify-between max-w-[300px] rounded-lg shadow-xl">
        <div className="overflow-hidden bg-gray-200 w-full aspect-w-4 aspect-h-3">
          <img
            src={img_url}
            alt={name}
            className="object-cover w-full h-full"
          />
        </div>
        <div className="flex justify-around items-center">
          <div className="mt-4">
            <h2 className="text-sm font-normal">{user}</h2>
            <h2 className="text-lg font-bold">{name}</h2>
          </div>
          <div className="flex gap-1 mt-3">
            <div>
              <img src={heart} width={25} />
              <h1 className="text-center">{likes}</h1>
            </div>

            <div>
              <img src={save} width={25} />
              <h1 className="text-center">{saves}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MixNMatchCard;
