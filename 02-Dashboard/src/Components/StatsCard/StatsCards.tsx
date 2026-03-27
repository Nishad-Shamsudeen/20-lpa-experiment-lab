import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGears } from '@fortawesome/free-solid-svg-icons';

export default function StatsCards() {
  const stats = [
    { label: 'Total Processes', value: 24 },
    { label: 'Success', value: 18 },
    { label: 'Failed', value: 3 },
    { label: 'Avg Runtime', value: '7.2 min' },
  ];
  return (
    <div className="mt-5 ">
      
      {/* {stats.map((item, i) => ( */}
      <div className="rounded-xl bg-blue-700 p-6 shadow">
        
        <p className="text-lg font-medium ">
          <FontAwesomeIcon icon={faGears} className="text-gray-400" />
          Total Processes
        </p>
        <p className="text-2xl font-normal">24</p>
      </div>
      <div className="rounded-xl bg-white p-6 shadow">
        <p className="text-lg font-medium ">
          <FontAwesomeIcon icon={faGears} className="text-gray-400" />
          Total Processes
        </p>
        <p className="text-2xl font-normal">24</p>
      </div>
      
      {/* // ))} */}
    </div>
  );
}
