import React from 'react'
import Ctech_Logo from '../assets/images/Ctech_Logo.png'

const GreyBar = () => {
  return (
    <div className="bg-gray-400 h-16 flex justify-center items-center">
      <img src={Ctech_Logo} className="h-8 w-auto" alt="CTech Logo" />
    </div>
  )
}

export default GreyBar

