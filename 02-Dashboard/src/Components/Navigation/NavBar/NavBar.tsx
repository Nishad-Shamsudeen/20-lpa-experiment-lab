import React, { useState } from 'react';
import { Bell, CircleUser, ChevronDown } from 'lucide-react';
import AuthMenu from '../AuthMenu/AuthMenu';

function NavBar({ open, setOpen }) {
  const [user, getUser] = useState<string | ''>('Nishad');
  const [isAuthMenu, setAuthMenu] = useState<boolean>(false);

  const toggleAuthMenu = (e) => {
    e.stopPropagation(); //
    setOpen((v) => !v);
  // console.log(open);
  };
  return (
    <>
      <nav className="bg-white shadow-sm">
        <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-6">
          {/* Left: Title */}
          <h1 className="text-lg font-bold">Monitoring Dashbord</h1>
          <div className="relative flex items-center gap-4 text-gray-700">
            <Bell className="h-5 w-5 cursor-pointer hover:text-black" />
            <CircleUser className="h-6 w-6 cursor-pointer" />
            <p className="font-bold">{user}</p>
            <ChevronDown
              className="h-4 w-4 cursor-pointer hover:text-black"
              onClick={toggleAuthMenu}
            />
            <AuthMenu open={open} setOpen={setOpen} />
          </div>
        </div>
        {/* <nav className="flex h-14 items-center justify-between bg-gray-100 px-10">

      </nav> */}

        {/* Right: Icons */}
      </nav>
    </>
  );
}

export default NavBar;
