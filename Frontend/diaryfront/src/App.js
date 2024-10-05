//import logo from './logo.svg';
import './App.css';
//import Login from './components/login/login';
import './re.js';
//const login() =><li>Username <span> 555</span></li>
import React from 'react';
import { BrowserRouter as Link } from 'react-router-dom';

function App() {
  
  //const design ={color:"#c16c2b"}
  return (
    <div className="login-container">

      <div className="login-form">
        <h2>Vigenere Diary</h2>

        <div className="input-group">
          <input
            type="text"
            placeholder="username"
          />
        </div>

        <div className="input-group2">
          <input
            type="text"
            placeholder="password"
          />

        </div>

        <div className="innerBox">
        <Link to="/re">
        <button>login</button>
        </Link>
        </div>

      </div>
    </div>

    
  ); 
}

export default App;
