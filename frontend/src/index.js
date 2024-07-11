import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Catalog from './pages/Catalog';
import MixNMatch from './pages/MixNMatch';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import StyleShowdown from './pages/StyleShowdown';
import ProductDetails from './pages/ProductDetails';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Navbar />
      <div className='h-[90vh]'>
      <Routes>
        <Route path="/" element={<App />}>
          <Route path="/women" element={<Catalog prod_type={"Women"} />} />
          <Route path="/men" element={<Catalog prod_type={"Men"} />} />
          <Route path="/accessories" element={<Catalog prod_type={"Accessories"} />} />
          <Route path="/product/:id" element={<ProductDetails />} />
          <Route path="/mixnmatch" element={<MixNMatch />} />
          <Route path="/styleshowdown" element={<StyleShowdown />} />
        </Route>
      </Routes>
      </div>
      <Footer />
    </BrowserRouter>
  </React.StrictMode>
);

reportWebVitals();
