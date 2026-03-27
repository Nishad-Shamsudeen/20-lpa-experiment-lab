import { useEffect, useState, useRef } from "react";

function Dashboard() {
  const [open, setOpen] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    const handleClick = (event) => {
      // OPTIONAL: ignore clicks inside menu

      
      if (menuRef.current && menuRef.current.contains(event.target)) {
        return;
      }
      setOpen(false);

    };

    document.addEventListener("click", handleClick);

    return () => {
      document.removeEventListener("click", handleClick);
    };
  }, []);

  return (
    <div>
      <button onClick={() => setOpen(true)}>Open Menu</button>
      <button>Test</button>

      {open && (
        <div ref={menuRef} className="menu">
          Menu content
        </div>
      )}
    </div>
  );
}
export default Dashboard
