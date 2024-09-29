import React from 'react';
import Card from './Card';
import { useEffect, useRef } from 'react';

const CompareCards = ({ selectedCards }) => {
  const comparisonRef = useRef(null);

  useEffect(() => {
    if (selectedCards.length === 2) {
      comparisonRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [selectedCards]);

  if (selectedCards.length !== 2) {
    return null;
  }

  return (
    <div ref={comparisonRef} className="comparison">
      <div className='text-center font-bold text-xl mb-2'>
      Comparison
      </div>
      <div className="flex flex-row justify-center w-auto h-auto gap-10">
        <Card id={selectedCards[0].candidate_id} title={selectedCards[0].name} rank={selectedCards[0].rank}  isSelected={true}/>
        <Card id={selectedCards[1].candidate_id} title={selectedCards[1].name} rank={selectedCards[1].rank} isSelected={true}/>
      </div>
    </div>
  );
};

export default CompareCards;
