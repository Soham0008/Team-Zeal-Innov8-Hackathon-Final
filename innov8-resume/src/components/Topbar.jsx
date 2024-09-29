import React from 'react';
import { Link } from 'react-router-dom';

const Topbar = () => {
  return (
    <>
      <div className="flex flex-wrap place-items-center ">
        <section className="relative mx-auto w-auto">
          {/* Navbar */}
          <nav className="flex justify-between bg-gray-900 text-white w-screen">
            <div className="px-5 xl:px-12 py-6 flex w-full items-center">
              <a className="text-3xl font-bold font-heading" >
                {/* <img className="h-9" src="logo.png" alt="logo"> */}
              </a>
              {/* Nav Links */}
              <ul className="hidden md:flex px-4 mx-auto font-semibold font-heading space-x-12">
                <li><a className="hover:text-gray-200" href="/home">Dashboard</a></li>
                <li><a className="hover:text-gray-200" href="/analytics">Analytics</a></li>
              </ul>
              {/* Header Icons */}
              <div className="hidden xl:flex items-center space-x-5">
              </div>
            </div>
          </nav>
        </section>
      </div>
    </>
  );
};

export default Topbar;