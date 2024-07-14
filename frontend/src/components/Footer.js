import React from 'react'
import github from "../assets/githublogo.png"
import figma from "../assets/figmalogo.png"
import { Link } from 'react-router-dom'

const Footer = () => {
  return (
    <div className='bg-black py-6 w-full text-white flex-col items-center justify-center'>
      <div className='flex items-center justify-center gap-4'>
        <Link to="https://github.com/amri-tah/MixNMatchStudio-Myntra"><img src={github} width={40}/></Link>
        <Link to="https://www.figma.com/proto/milkChhGO0yHKmKAgWtEIt/WeForShe24-InnovateHers?node-id=192-16&t=DOtBIIz6m957XMcQ-1&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1"><img src={figma} width={27}/></Link>
      </div>
        <div className='w-fit mx-auto mt-3'>Made with ❤️ by Team InnovateHers</div>
      
    </div>
  )
}

export default Footer
