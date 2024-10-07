/*import React, { useEffect } from 'react';
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
    navigate('/');
  }, [token, location.pathname, navigate]);

  return (
    <div className="App">
      {/* Show Navbar on all pages except Login and Register }
      
      
      <Routes>
        <Route path="/login" element={<Login />} />
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
*/
// import React from 'react';
// import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
// import Login from './components/Login.js';
// ///import About from './components/About.js';
// //import About from './About';
// //import Contact from './Contact';

// const App = () => {
//   return (
//     <Router>
//       <nav>
//         <ul>
//           <li>
//             <Link to="/">Login</Link>
//           </li>
//            {/* <li>
//             <Link to="/about">About</Link>
//           </li>
//           {/* <li>
//             <Link to="/contact">Contact</Link>
//           </li>  */} 
//         </ul>
//       </nav>

//       <Routes>
//         <Route path="/" element={<Login />} />
//        {/* <Route path="/about" element={<About />} />
//         <Route path="/contact" element={<Contact />} />  */}
//       </Routes>
//     </Router>
//   );
// };

// export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import login from './components/login.js';
//import About from './About';
//import Contact from './Contact';

const App = () => {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">login</Link>
          </li>
          
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<login />} />
        
      </Routes>
    </Router>
  );
};

export default App;