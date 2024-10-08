// db.js
const { Pool } = require('pg');

const pool = new Pool({
  user: 'adminSecure',     // ชื่อผู้ใช้
  host: '127.0.0.1',      // ที่อยู่โฮสต์
  database: 'dbdiary',    // ชื่อฐานข้อมูล
  password: 'pass1234',    // รหัสผ่าน
  port: 5432,              // พอร์ต (ค่าเริ่มต้นของ PostgreSQL)
});

// ฟังก์ชันสำหรับเชื่อมต่อและทดสอบฐานข้อมูล
pool.connect((err) => {
  if (err) {
    console.error('Error connecting to the database', err);
  } else {
    console.log('Connected to the database successfully!');
  }
});

module.exports = pool;



// DATABASES = {
//     'default': {
//         'ENGINE': 'django.db.backends.postgresql',
//         'NAME': 'dbdiary',
//         'USER': 'adminSecure',
//         'PASSWORD': 'pass1234',
//         'HOST': '127.0.0.1',  # 127.0.0.1 or localhost
//         'PORT': '5432',
//     }
// }