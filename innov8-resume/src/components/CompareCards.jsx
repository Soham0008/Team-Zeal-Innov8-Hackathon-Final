import React from 'react';
import Card from './Card';

const CompareCards = () => {
  const card1 = { id: 1, title: 'Card 1', description: 'This is the first card.' };
  const card2 = { id: 2, title: 'Card 2', description: 'This is the second card.' };

  return (
    <div className="py-10 bg-gradient-to-r min-h-screen from-blue-500 to-purple-600">
        <div className='text-center font-bold text-xl mb-2'>
            Comparison Between these two Candidates
        </div>
    <div className='flex justify-center space-x-40 mt-10'>
      <Card id={card1.id} title={card1.title} description={card1.description} />
      <div className='text-center justify-center font-bold text-xl mb-2 mt-10'>
        VS
      </div>
      <Card id={card2.id} title={card2.title} description={card2.description} />
      </div>
    </div>
  );
}

export default CompareCards;
