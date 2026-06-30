import React from 'react';
import NavBar from '../../Components/Navigation/NavBar/NavBar';
import SideBar from '../../Components/Navigation/SideBar/sideBar';
import StatsCards from '../../Components/StatsCard/StatsCards';
import ProcessList from '../../Components/ProcessList/ProcessList'
import './Dashboard.css';

function Dashboard({ open, setOpen }) {
  return (
    <div className="flex h-screen flex-col">
      <NavBar open={open} setOpen={setOpen} />
      {/* Sidebar and main content side by side */}
      <div className="flex">
        <SideBar />
        <main className="w-full bg-gray-50">
          <div className="main-container flex justify-around">
            <StatsCards label={'Total Process'} value={10}/>
            <StatsCards label={'Success'} value={11}/>
            <StatsCards label={'Failed'} value={13}/>
            <StatsCards label={'Avg Runtime'} value={12}/>
          </div>
          <div className='flex justify-center proces-table' >
            <ProcessList/>
          </div>

          {/* Your dashboard content goes here */}
        </main>
      </div>
    </div>
  );
}

export default Dashboard;
