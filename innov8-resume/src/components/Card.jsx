import React from 'react';

const Card = ({ id, title, rank, isSelected}) => {
  return (
    <div className={`max-w-sm rounded overflow-hidden shadow-lg ${isSelected ? 'bg-blue-100 border-blue-500' : 'bg-white'}`}>
      <div className="w-full text-center font-bold text-xl mb-2">
        Candidate No. {id}<br />
        Candidate Rank {rank}
        <br /><br />{rank > 904 ? (
              <span style={{ color: 'red' }}> 🚩<br></br>
              RED FLAG!!</span>
            ) : (
              <span style={{ color: 'green' }}> ✅<br></br>
              GREEN FLAG!!</span>
            )}
            <br /><br /><br /><br /><br /><br />
      </div>
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{title}</div>
        <p className="text-gray-700 text-base">
        </p>
      </div>
      <div className="px-6 pt-4 pb-2">
        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag1</span>
        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag2</span>
        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag3</span>
      </div>
    </div>
  );
}

export default Card;
