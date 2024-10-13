// ฟังก์ชันเข้าสู่ระบบ (Login)
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // สร้างข้อมูลที่ต้องการส่ง
    const data = {
        username: username,
        password: password
    };

    // ส่งข้อมูลไปที่เซิร์ฟเวอร์
    fetch('http://127.0.0.1:8000/vigenere-diary/login/', {
        method: 'POST', // ใช้เมธอด POST
        headers: {
            'Content-Type': 'application/json' // กำหนดให้เป็น JSON
        },
        body: JSON.stringify(data) // แปลงข้อมูลเป็น JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Login failed');
        }
        return response.json();
    })
    .then(result => {
        //alert(`Welcome, ${username}!`); // แสดงข้อความต้อนรับเมื่อเข้าสู่ระบบสำเร็จ
        document.location.href = 'new-diary.html'; // ไปยังหน้า new-diary หลังจากเข้าสู่ระบบ
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Login failed. Please try again.');
    });
}

// ฟังก์ชันสมัครสมาชิก (Register)
function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirm-password').value;
    // ตรวจสอบว่ารหัสผ่านและการยืนยันรหัสผ่านตรงกัน
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    // สร้างข้อมูลที่ต้องการส่ง
    const data = {
        username: username,
        password: password
    };

    // ส่งข้อมูลไปที่เซิร์ฟเวอร์
    fetch('http://127.0.0.1:8000/vigenere-diary/users/', {
        method: 'POST', // ใช้เมธอด POST
        headers: {
            'Content-Type': 'application/json' // กำหนดให้เป็น JSON
        },
        body: JSON.stringify(data) // แปลงข้อมูลเป็น JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to register');
        }
        return response.json();
    })
    .then(result => {
        //alert(`Account created for ${username}!`);
        document.location.href = 'index.html'; // กลับไปที่หน้า Login หลังจากสมัครเสร็จ
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Registration failed. Please try again.');
    });
    }
// // Register Form Handling
// $("#registerForm").submit(function(event) {
//     event.preventDefault(); // ป้องกันการรีเฟรชหน้า
//     let username = $("#registerUsername").val();
//     let password = $("#registerPassword").val();
    
//     // ส่งข้อมูลไปยังเซิร์ฟเวอร์
//     $.ajax({
//       url: 'http://127.0.0.1:8000/vigenere-diary/users/', 
//       type: 'POST',
//       contentType: 'application/json', // กำหนด content type เป็น JSON
//       data: JSON.stringify({ username: username, password: password }), // ส่งข้อมูลในรูปแบบ JSON

//       success: function(response) {
//         alert('Registration successful!'); // แสดงข้อความเมื่อสมัครสมาชิกสำเร็จ
//         // ดำเนินการต่อ เช่น เปลี่ยนหน้า
//       },
//       error: function(xhr) {
//         console.error(xhr.responseText); // แสดงข้อความผิดพลาดใน console
//         alert('Registration failed! Please try again.'); // แสดงข้อความเมื่อสมัครสมาชิกไม่สำเร็จ
//       }
//     })


// ฟังก์ชันสำหรับบันทึกไดอารี่ใหม่
function saveDiary() {
    const topic = document.getElementById('topic').value;
    const content = document.getElementById('content').value;
    const secretKey = document.getElementById('secret-key').value;

    // เข้ารหัสเนื้อหาแบบ Base64
    const encryptedContent = btoa(content); 

    // สร้างข้อมูลที่ต้องการส่ง
    const data = {
        topic: topic,
        content: encryptedContent,
        secret_key: secretKey
    };

    // ส่งข้อมูลไปที่เซิร์ฟเวอร์
    fetch('http://127.0.0.1:8000/vigenere-diary/diaries/', {
        method: 'POST', // ใช้เมธอด POST
        headers: {
            'Content-Type': 'application/json', // กำหนดให้เป็น JSON
        },
        body: JSON.stringify(data) // แปลงข้อมูลเป็น JSON ก่อนส่ง
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to save diary');
        }
        return response.json();
    })
    .then(result => {
        //alert('บันทึกไดอารี่เรียบร้อยแล้ว!'); // แสดงข้อความเมื่อบันทึกสำเร็จ
        document.location.href = 'view-diary.html'; // เปลี่ยนหน้าไปยัง view-diary.html
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to save diary. Please try again.');
    });
}


// ฟังก์ชันสำหรับแสดงรายการไดอารี่ทั้งหมด
function loadDiaries() {
    const diaryList = document.getElementById('diary-list');
    let diaries = JSON.parse(localStorage.getItem('diaries')) || [];

    diaries.forEach((diary, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>หัวข้อ:</strong> ${diary.topic}
            <button onclick="viewDiary(${index})">ดู</button>
        `;
        diaryList.appendChild(li);
    });
}

// ฟังก์ชันสำหรับดูไดอารี่เดี่ยว
function viewDiary(index) {
    let diaries = JSON.parse(localStorage.getItem('diaries')) || [];
    const diary = diaries[index];

    const secretKey = prompt('กรุณาใส่กุญแจลับเพื่อถอดรหัส:');

    if (secretKey === diary.secretKey) {
        const decryptedContent = atob(diary.content);
        //alert(`เนื้อหาไดอารี่: ${decryptedContent}`);
    } else {
        alert('กุญแจลับไม่ถูกต้อง!');
    }
}

// ฟังก์ชันสำหรับสลับการแสดงเมนูบนมือถือ
function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'flex';
    } else {
        sidebar.style.display = 'none';
    }
}

// ฟังก์ชันสำหรับปุ่มย้อนกลับ
function goBack() {
    window.history.back();
}

// โหลดไดอารี่เมื่ออยู่ที่หน้า view-diary.html
if (document.getElementById('diary-list')) {
    loadDiaries();
}

