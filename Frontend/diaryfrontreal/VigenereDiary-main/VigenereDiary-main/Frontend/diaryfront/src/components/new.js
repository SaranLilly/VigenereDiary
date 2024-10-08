import React from 'react';
import "./new.css";
// import React from 'react';
import { BrowserRouter as Link } from 'react-router-dom';


const New = () => {
  return <div className="login-container">

     <div className="input-group">
       <input
         type="text"
         placeholder="Topic"
       />
     </div> 

    <div className="login-cont">

    <div class="background-cont">
    {/* <h1 class="text1">Vigenere Diary</h1> */}

    <div class="background-container">
    <h2 class="text">My Diary</h2>

    <div className="innerBox">
     <Link >
    <button>New Diary</button>
     </Link>
     </div>

     <div className="innerBox">
     <Link >
    <button>View All Entries</button>
     </Link>
     </div>
    
      
    </div>
    </div>
    </div>
  </div>
};


export default New;