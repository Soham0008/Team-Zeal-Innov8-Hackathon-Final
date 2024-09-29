// src/App.js
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Analytics from './pages/Analytics';

const App = () => {
  return (
    <BrowserRouter>
    <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/home" element={<Home/>} />
            <Route path="/analytics" element={<Analytics/>} />
    </Routes>
    </BrowserRouter>
  );
};

export default App;
