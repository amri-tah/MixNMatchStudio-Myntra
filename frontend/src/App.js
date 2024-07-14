import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import landing from "./assets/landing.png";

function App() {
  const location = useLocation();

  return (
    <div>
      <Outlet />
      {location.pathname === '/' && (
        <div>
          <img src={landing} className='w-full' alt="Landing" />
        </div>
      )}
    </div>
  );
}

export default App;
