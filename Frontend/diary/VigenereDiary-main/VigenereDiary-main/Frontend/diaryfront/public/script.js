// ฟังก์ชันเข้าสู่ระบบ (Login)
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // ไม่ทำการตรวจสอบรหัสผ่าน เพียงแค่บันทึกผู้ใช้แล้วเข้าสู่ระบบ
    alert(`Welcome, ${username}!`);
    document.location.href = 'new-diary.html';
}

// ฟังก์ชันสมัครสมาชิก (Register)
function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirm-password').value;

    alert(`Account created for ${username}!`);
    document.location.href = 'index.html'; // กลับไปที่หน้า Login หลังจากสมัครเสร็จ
}

// ฟังก์ชันสำหรับบันทึกไดอารี่ใหม่
function saveDiary() {
    const topic = document.getElementById('topic').value;
    const content = document.getElementById('content').value;
    const secretKey = document.getElementById('secret-key').value;

    const encryptedContent = btoa(content); // เข้ารหัสแบบ Base64

    let diaries = JSON.parse(localStorage.getItem('diaries')) || [];
    diaries.push({ topic, content: encryptedContent, secretKey });
    localStorage.setItem('diaries', JSON.stringify(diaries));

    alert('บันทึกไดอารี่เรียบร้อยแล้ว!');
    document.location.href = 'view-diary.html';
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
        alert(`เนื้อหาไดอารี่: ${decryptedContent}`);
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

