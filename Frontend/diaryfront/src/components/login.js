// import "./login.css";
// import React from 'react';
// import { BrowserRouter as Link,useNavigate } from 'react-router-dom';

// function Login() {
//     const navigate = useNavigate();
//   return (
    // <div className="login-container">

    //   <div className="login-form">
    //     <h2>Vigenere Diary</h2>

    //     <div className="input-group">
    //       <input
    //         type="text"
    //         placeholder="username"
    //       />
    //     </div>

    //     <div className="input-group2">
    //       <input
    //         type="text"
    //         placeholder="password"
    //       />

    //     </div>

    //     <div className="innerBox">
    //     <Link to="/re">
    //     <button>login</button>
    //     </Link>
    //     </div>

    // <button onClick={() => navigate("/re")} style={{ cursor: 'pointer', color: 'blue', textDecoration: 'underline' }}>
    // Register
    //  </button>

        
    //   </div>
    // </div>

    
//   );
//   }
  
//   export default Login;

import React from 'react';
import "./login.css";
// import React from 'react';
import { BrowserRouter as Link } from 'react-router-dom';
import Re from './Re.js';

const Login = () => {
  return <div className="login-container">

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
    <Link to="/Re">
    <button>login</button>
    </Link>
    </div>

    
  </div>
</div>
};

export default Login;

// import React from 'react';
// import "./login.css";
// // import React from 'react';
// import { BrowserRouter as Link } from 'react-router-dom';


// const Login = () => {
//   return <div className="login-container">

//      <div className="input-group">
//        <input
//          type="text"
//          placeholder="Topic"
//        />
//      </div> 

//     <div className="login-cont">

//     <div class="background-cont">
//     {/* <h1 class="text1">Vigenere Diary</h1> */}

//     <div class="background-container">
//     <h2 class="text">My Diary</h2>

//     <div className="innerBox">
//      <Link >
//     <button>New Diary</button>
//      </Link>
//      </div>

//      <div className="innerBox">
//      <Link >
//     <button>View All Entries</button>
//      </Link>
//      </div>
    
      
//     </div>
//     </div>
//     </div>
//   </div>
// };


// export default Login;