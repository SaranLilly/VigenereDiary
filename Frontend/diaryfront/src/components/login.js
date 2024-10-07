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
 import "./login.css";
// import React from 'react';
 import { BrowserRouter as Link } from 'react-router-dom';
import React from 'react';

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
    <Link to="/re">
    <button>login</button>
    </Link>
    </div>

    
  </div>
</div>
};

export default Login;