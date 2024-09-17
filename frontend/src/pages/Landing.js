import React from 'react'
import Navbar from '../components/Navbar'
import AlertBar from '../components/AlertBar'
import MockMe from '../assets/images/LogoBlack.png'
import GreyBar from '../components/GreyBar'
import Puzzle from '../assets/images/puzzle.png'
import Pfp from '../assets/images/pfp.png'
import Calendar from '../assets/images/calendar.png'
import FooterBar from '../components/FooterBar'

export default function Landing() {
  return (
    <div>
    <div className="fixed top-0 left-0 right-0 z-50">
      <Navbar />
      <AlertBar/>
    </div>
    <div className="flex justify-center mt-60 mb-10">
      <img src={MockMe} className="h-28 w-auto" alt="MockMe logo" />
    </div>
        <div className="text-center mt-6">
          <h1 className="text-6xl font-bold">Mock with Peers from Your Campus</h1>
          <p className="text-center text-2xl mt-12 mb-6">Match with Campus Peers for Interactive Technical Practice and Achieve Interview Success.</p>
          <button className="bg-red-500 text-white text-2xl  px-8 py-4 rounded-md mt-16" onClick={() => {window.location.href = "/register";}}>Find Your Match</button>
        </div>
        <div className="mt-48">
          <GreyBar />
        </div>
        <div className="mt-24 text-center mx-16 mb-20 md:mx-0">
          <h2 className="text-4xl font-bold">Key Features</h2>
          <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-x-12 gap-y-8">
            <div className="flex flex-col items-center">
              <h2 className="text-3xl font-bold">Smart Match-Making</h2>
              <p className="mt-2 mx-10 text-xl">Get matched with peers who have similar interests and goals for targeted practice.</p>
              <img src={Puzzle} className="h-12 w-auto mt-12" alt="MockMe logo" />
            </div>
            <div className="flex flex-col items-center">
              <h2 className="text-3xl font-bold">Seamless Scheduling</h2>
              <p className="mt-2 mx-10 text-xl">Integrate with Google Calendar to easily find and book available times.</p>
              <img src={Calendar} className="h-12 w-auto mt-12" alt="MockMe logo" />
            </div>
            <div className="flex flex-col items-center">
              <h2 className="text-3xl font-bold">Detailed Profiles</h2>
              <p className="mt-2 mx-10 text-xl">View detailed profiles to find the best match for your  preparation needs.</p>
              <img src={Pfp} className="h-12 w-auto mt-12" alt="MockMe logo" />
            </div>
          </div>
        </div>
        <FooterBar />
    </div>
  )
}

