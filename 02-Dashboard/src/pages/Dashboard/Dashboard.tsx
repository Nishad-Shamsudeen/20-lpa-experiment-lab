import React from 'react';
import NavBar from '../../Components/Navigation/NavBar/NavBar';
import SideBar from '../../Components/Navigation/SideBar/sideBar';
import StatsCards from '../../Components/StatsCard/StatsCards';

function Dashboard({ open, setOpen }) {
  return (
    <div className="flex h-screen flex-col">
      <NavBar open={open} setOpen={setOpen} />
      {/* Sidebar and main content side by side */}
      <div className="flex flex-1 overflow-hidden">

      <SideBar/>
      <main className="flex-1 overflow-y-auto bg-gray-50">
          {/* Your dashboard content goes here */}
         <StatsCards/>
        </main>
      </div>
    </div>
  );
}

export default Dashboard;
