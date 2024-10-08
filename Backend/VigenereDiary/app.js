const express = require('express'); // นำเข้า express
const bodyParser = require('body-parser'); // นำเข้า body-parser
const cors = require('cors'); // นำเข้า cors
const bcrypt = require('bcrypt'); // นำเข้า bcrypt
const app = express(); // สร้าง instance ของ express

const pool = require('./db'); // นำเข้าไฟล์เชื่อมต่อฐานข้อมูล
const PORT = 8000; // กำหนดพอร์ต

// Middleware
app.use(cors()); // เปิดใช้งาน CORS
app.use(bodyParser.json()); // ใช้ body-parser สำหรับการ parse JSON body

// Route สำหรับการลงทะเบียนผู้ใช้
app.post('/vigenere-diary/users/', async (req, res) => {
    const { username, password } = req.body; // รับข้อมูลจาก body
    
    console.log(`Username: ${username}, Password: ${password}`); // แสดงข้อมูลใน console

    try {
        // Hash รหัสผ่าน
        const hashedPassword = await bcrypt.hash(password, 10);

        // บันทึกข้อมูลผู้ใช้ลงฐานข้อมูล
        const result = await pool.query(
            'INSERT INTO users_user (username, password) VALUES ($1, $2) RETURNING *',
            [username, hashedPassword]
        );

        res.status(201).json({ message: 'Registration successful!', user: result.rows[0] }); // ส่งข้อความกลับ
    } catch (error) {
        console.error('Error saving user to the database', error);
        res.status(500).json({ error: 'Error registering user' }); // ส่งข้อความผิดพลาดกลับ
    }
});

// Route สำหรับการเข้าสู่ระบบ
app.post('/vigenere-diary/login/', async (req, res) => {
    const { username, password } = req.body; // รับข้อมูลจาก body
    console.log(`Username: ${username}, Password: ${password}`); // แสดงข้อมูลใน console

    try {
        const result = await pool.query(
            'SELECT * FROM users_user WHERE username = $1',
            [username]
        );

        if (result.rows.length > 0) {
            const user = result.rows[0];
            // ตรวจสอบรหัสผ่าน
            const match = await bcrypt.compare(password, user.password);

            if (match) {
                res.json({ message: 'Login successful!', user: user }); // ส่งข้อความกลับ
            } else {
                res.status(401).json({ error: 'Invalid username or password' }); // ส่งข้อความผิดพลาดกลับ
            }
        } else {
            res.status(401).json({ error: 'Invalid username or password' }); // ส่งข้อความผิดพลาดกลับ
        }
    } catch (error) {
        console.error('Error logging in', error);
        res.status(500).json({ error: 'Error logging in' }); // ส่งข้อความผิดพลาดกลับ
    }
});

// เริ่มเซิร์ฟเวอร์
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`); // แสดงข้อความเมื่อเซิร์ฟเวอร์เริ่มทำงาน
});
