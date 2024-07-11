import React from 'react'
import logo from "../assets/logo.png"
import { Link } from 'react-router-dom'
const Navbar = () => {
  return (
    <div className='flex py-6 px-10 shadow-lg gap-10 text-sm'>
      <Link to="/"><img src={logo} width={60} alt='logo' className='ml-10'/></Link>
      <div className='flex gap-10 items-center font-semibold'>
        <Link to="/women">WOMEN</Link>
        <Link to="/men">MEN</Link>
        <Link to="/accessories">ACCESSORIES</Link>
        <Link to="/mixnmatch">MIX & MATCH STUDIO</Link>
      </div>
    </div>
  )
}

export default Navbar
