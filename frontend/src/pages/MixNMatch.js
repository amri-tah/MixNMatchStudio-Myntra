import React from 'react'
import { Link } from 'react-router-dom'
import mixnmatch from "../assets/mixnmatch.png"
import mic from '../assets/mic.png'
import MixNMatchCard from '../components/MixNMatchCard'
import axios from 'axios';
import { useState, useEffect } from 'react';

const MixNMatch = () => {
  const [collections, setCollections] = useState([]);

  useEffect(() => {
    const fetchMixnmatchCollections = async () => {
      try {
        const response = await axios.get('/mixnmatch/');
        setCollections(response.data);
      } catch (error) {
        console.error('Error fetching canvas:', error);
      }
    };

    fetchMixnmatchCollections();
  }, []);

  return (
    <div>
      <div className='p-3 text-center bg-gradient-to-r from-[#E588B8] to-[#FF8F2B] text-white'>Style Showdown: Retro Picnic - Starting July 5th! <Link to="/styleshowdown">Click Here to Learn More</Link></div>
      <div className='flex items-center'>
        <div className='w-[60%] p-10 ml-[5%]'>
          <h1 className='text-[1.5rem] leading-[90%]'>INTRODUCING</h1>
          <h1 className="text-[3rem] font-bold leading-[90%] w-fit bg-clip-text text-transparent bg-gradient-to-r from-[#E588B8]  to-[#FF8F2B]">
      Mix&Match <br/>Studio
    </h1>
    <h1 className='text-[1.5rem] mt-4 leading-[90%]'>Unleash Your Style, <br/>
    One Combination at a Time 🎨💃</h1>
    <h1 className="bg-[#D9D9D9] px-4 py-2 rounded-lg text-lg w-fit mt-6">Create Your Look!</h1>

        </div>
        <div className='w-[40%] bg-blue'>
          <img src={mixnmatch} width={600} alt="landing page"/>
        </div>
      </div>

      <div className="flex gap-3 items-center justify-center my-[5%]">
        <div><img src={mic} width={190} alt="Microphone" /></div>
        <div>
          <h1 className="text-[1.5rem]">Calling All Fashion Enthusiasts to</h1>
          <h1 className="text-[3rem] font-bold leading-6">
            Style Showdown!
          </h1>
          <Link to="/styleshowdown"><h1 className="bg-[#E7C93A] px-4 py-2 rounded-lg text-lg w-fit mt-6">Learn More</h1></Link>
          
        </div>
      </div>

      <div className='p-10 ml-[3%]'>
      <h1 className="text-[1.8rem] ">TRENDING CANVAS</h1>
      <div className='grid grid-cols-4 sm:grid-cols-2 lg:grid-cols-4 gap-2'>
      {collections.map((collection) => (
          <Link key={collection.id} to={`/collection/${collection.id}`} className="flex justify-center">
            <MixNMatchCard key={collection.id} name={collection.name} img_url={collection.img_url} user={collection.user} likes={collection.likes} saves={collection.saves} />
          </Link>
        ))}
      </div>
      
      </div>
    </div>
  )
}

export default MixNMatch
