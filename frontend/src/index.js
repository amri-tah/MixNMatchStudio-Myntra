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
      <Navbar/>
      <Routes>
        <Route path="/" element={<App />}>
          <Route path="women" element={<Catalog />} />
          <Route path="men" element={<Catalog />} />
          <Route path="accessories" element={<Catalog />} />
          <Route path="/product/:id" component={<ProductDetails/>} />
          <Route path="mixnmatch" element={<MixNMatch />} />
          <Route path="styleshowdown" element={<StyleShowdown/>} />
        </Route>
      </Routes>
      <Footer/>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
