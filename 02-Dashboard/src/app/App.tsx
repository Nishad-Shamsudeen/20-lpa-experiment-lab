import React, { useState } from "react";
import "./App.css";
import NavBar from "../Components/Navigation/NavBar/NavBar";
// import Dashboard from "../DashboardTempDeleteThisAfterComplete"
import SideBar from "../Components/Navigation/SideBar/sideBar";
import Dashboard from "../pages/Dashboard/Dashboard";
function App() {
  const [open, setOpen] = useState<boolean>(false);
  return (
     <div className="min-h-screen">
      <Dashboard open={open} setOpen={setOpen}/>
      {/* <NavBar open={open} setOpen={setOpen} />
      <SideBar/> */}
    </div>
  );
}

export default App;
