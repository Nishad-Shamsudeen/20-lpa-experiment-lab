import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGears } from '@fortawesome/free-solid-svg-icons';
import './StatsCard.css'

export default function StatsCards({label,value}) {
 
  return (
    <div className="flex justify-around main-container ">
      
      {/* {stats.map((item, i) => ( */}
      <div className="rounded-xl bg-white w-40 shadow">
        
        <p className="text-lg font-medium ">
          <FontAwesomeIcon icon={faGears} className="text-gray-400" />
          {label}
        </p>
        <p className="text-2xl font-normal">{value}</p>
      </div>
     
      
      {/* // ))} */}
    </div>
  );
}
