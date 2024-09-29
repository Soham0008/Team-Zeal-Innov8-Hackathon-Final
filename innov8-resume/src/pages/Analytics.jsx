// import React from 'react';
// import Topbar from '../components/Topbar';
// import CompareCards from '../components/CompareCards';

// const Analytics = () => {

//   return(
//     <><Topbar />
//     <CompareCards /></>
//   );
// }

// export default Analytics;

import React, { useState } from 'react';
import CardList from '../components/CardList';
import CompareCards from '../components/CompareCards';
import Topbar from '../components/Topbar';
import cards from '../final.json'

const Analytics = () => {
  const [selectedCards, setSelectedCards] = useState([]);


  const handleCardClick = (card) => {
    if (selectedCards.length < 2) {
      setSelectedCards([...selectedCards, card]);
    } else {
      alert('You can only compare two cards at a time.');
    }
  };

  return (
    <div className='min-h-screen bg-gradient-to-r from-blue-500 to-purple-600'>
      <Topbar/>
      <CardList cards={cards} onCardClick={handleCardClick} selectedCards={selectedCards} />
      <CompareCards selectedCards={selectedCards} />
    </div>
  );
};

export default Analytics;
