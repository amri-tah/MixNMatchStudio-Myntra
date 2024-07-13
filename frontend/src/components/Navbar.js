import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import canvas from '../assets/Flipboard.png';
import cart from '../assets/Cart.png';
import heart from '../assets/HeartNav.png';
import profile from '../assets/User.png';

const Navbar = () => {
  const navItems = [
    { icon: cart, text: 'Cart', link: '/' },
    { icon: canvas, text: 'Canvas', link: '/' },
    { icon: heart, text: 'Wishlist', link: '/wishlist' },
    { icon: profile, text: 'Profile', link: '/profile' },
  ];

  return (
    <div className='flex justify-between w-full py-6 px-10 shadow-lg'>
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
      
      
      <ul className='flex ml-[500px] items-center gap-5'> 
        {navItems.map((item) => (
          <li key={item.text}>
            <Link to={item.link}>
              <img src={item.icon} alt={item.text} className='w-6 h-6 mr-2' />
              <span>{item.text}</span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
    </div>
  );
};

export default Navbar;
