import React, { useState } from 'react';
import Card from './Card';

const CardList = ({ cards, onCardClick, selectedCards }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredCards = cards.filter((card) =>
    card.candidate_id.toString().includes(searchTerm) && !selectedCards.includes(card)
  );

  return (
    <div className="p-4">
      <input
        type="text"
        placeholder="Search cards by ID..."
        value={searchTerm}
        onChange={handleSearch}
        className="mb-4 p-2 border border-gray-300 rounded w-full"
        disabled={selectedCards.length === 2}
      />
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 overflow-hidden">
        {filteredCards.map((card) => (
          <div key={card.candidate_id} onClick={() => onCardClick(card)} className="cursor-pointer">
            <Card id={card.candidate_id} title={card.name} rank={card.rank} isSelected={false} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default CardList;
