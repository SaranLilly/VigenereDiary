import React from 'react';
import New from './New'; // ให้แน่ใจว่าชื่อไฟล์ตรง

function Re() {
  return <div className="login-container">

  <div className="login-form">
    <h2>Register</h2>

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

    <div className="input-group3">
      <input
        type="text"
        placeholder="Confirm password"
      />
    </div>

    <div className="innerBox">
    <Link to="/New">
    <button>Register</button>
    </Link>
    </div>


  </div>
  </div>
}

export default Re;