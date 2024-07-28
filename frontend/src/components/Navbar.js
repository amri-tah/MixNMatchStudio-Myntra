import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import logo from '../assets/logo.png';
import canvas from '../assets/Flipboard.png';
import cart from '../assets/Cart.png';
import heart from '../assets/HeartNav.png';
import profile from '../assets/User.png';
import search from '../assets/search.png'

const Navbar = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const navItems = [
    { icon: cart, text: 'Cart', link: '/' },
    { icon: canvas, text: 'Canvas', link: '/' },
    { icon: heart, text: 'Wishlist', link: '/wishlist' },
    { icon: profile, text: 'Profile', link: '/profile' },
  ];

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?query=${searchQuery}`);
    }
  };

  return (
    <div className='sticky top-0 z-50 bg-white shadow-lg'>
      <div className='flex justify-between w-full py-6 px-10'>
        <div className='flex gap-10 text-sm'>
          <Link to="/">
            <img src={logo} width={60} alt='logo' className='ml-10' />
          </Link>
          <div className='flex gap-10 items-center font-semibold'>
            <Link to="/women">WOMEN</Link>
            <Link to="/men">MEN</Link>
            <Link to="/accessories">ACCESSORIES</Link>
            <Link to="/mixnmatch">MIX & MATCH STUDIO</Link>
          </div>
        </div>
        
        <ul className='flex ml-[50px] items-center gap-5'>
          <li><form onSubmit={handleSearch} className='flex items-center mr-5'>
          <input
            type='text'
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder='Search for products...'
            className='border rounded-l-md px-4 py-2 w-[300px]'
          />
          <button type='submit' className='bg-black text-white px-4 py-2 rounded-r-md'>
          <img src={search} alt="search" width={25} />
          </button>
        </form></li>
          {navItems.map((item) => (
            <li key={item.text}>
              <Link to={item.link} className='flex flex-col items-center justify-center'>
                <img src={item.icon} alt={item.text} className='w-6 h-6 mb-1' />
                <span className='text-md'>{item.text}</span>
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
