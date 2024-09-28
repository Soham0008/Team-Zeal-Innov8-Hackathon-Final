import React from 'react';
import Topbar from '../components/Topbar';
import CardSlider from '../components/CardSlider';

const Home = () => {
  return(
  <><Topbar />
  <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-blue-500 to-purple-600">
      <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-lg shadow-lg p-8 max-w-md w-full">
        <CardSlider/>
      </div>
    </div>
    </>
  ); 
};

export default Home;