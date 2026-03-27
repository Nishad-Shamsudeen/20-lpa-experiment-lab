import clsx from 'clsx';
import React, { useEffect, useRef, useState } from 'react'

function AuthMenu({open,setOpen}) {
  const menuRef = useRef<HTMLDivElement |null>(null)
 
  const handleClick=(event: MouseEvent)=>{
     if ( menuRef.current && !menuRef.current.contains(event.target as Node)) {
      setOpen(false);
      console.log("Outside clicked")
    }
  // alert("Clicked")

  }
  useEffect(()=>{
    if (!open) return;
      document.addEventListener("click",handleClick)
      return ()=>{
        document.removeEventListener("click",handleClick)
      }
  },[open])
  const base= "w-50 h-50 bg-gray-100 rounded-md absolute right-[27px] top-[70px] shadow-xl transition-all duration-200 ease-out"
  const openCls = "opacity-100 scale-100 translate-y-0 pointer-events-auto";
  return (
    <>
    
    <div ref={menuRef}className={clsx(base,
      open && openCls,
      !open && "opacity-0 scale-95 -translate-y-2 pointer-events-none") }>AuthMenu</div>

    
    </>

  )
}

export default AuthMenu