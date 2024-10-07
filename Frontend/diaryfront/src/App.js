import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation, useNavigate } from 'react-router-dom';
//import Navbar from './components/navbar/navbar';
import Login from './components/login.js';
//import Register from './components/register/register';
//import FeedPage from './components/feed/FeedPage.js';
//import ProfilePage from './components/profile/ProfilePage.js';
//import ProfileFriendPage from './components/profile/ProfileFriendPage.js';
//import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const location = useLocation();
  const navigate = useNavigate();
  const token = localStorage.getItem('token'); // Get token from localStorage

  // Redirect to login if there's no token
  useEffect(() => {
    
  }, [token, location.pathname, navigate]);

  return (
    <div className="App">
      {/* Show Navbar on all pages except Login and Register */}
      
      
      <Routes>
        <Route path="/" element={<Login />} />
      </Routes>
    </div>
  );
}

export default function AppWithRouter() {
  return (
    <Router>
      <App />
    </Router>
  );
}

