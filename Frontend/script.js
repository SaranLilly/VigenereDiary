// Login Form Handling
$("#loginForm").submit(function(event) {
    event.preventDefault(); // ป้องกันการรีเฟรชหน้า
    let username = $("#loginUsername").val();
    let password = $("#loginPassword").val();
    
    // ส่งข้อมูลไปยังเซิร์ฟเวอร์ (mock AJAX request)
    $.ajax({
      url: 'http://127.0.0.1:8000/vigenere-diary/login/', 
      type: 'POST',
      data: { username: username, password: password },
      success: function(response) {
        alert('Login successful!');
        // ดำเนินการต่อ เช่น เปลี่ยนหน้า
      },
      error: function() {
        alert('Login failed! Please check your username and password.');
      }
    });
  });
  
// Register Form Handling
$("#registerForm").submit(function(event) {
    event.preventDefault(); // ป้องกันการรีเฟรชหน้า
    let username = $("#registerUsername").val();
    let password = $("#registerPassword").val();
    
    // ส่งข้อมูลไปยังเซิร์ฟเวอร์
    $.ajax({
      url: 'http://127.0.0.1:8000/vigenere-diary/users/', 
      type: 'POST',
      contentType: 'application/json', // กำหนด content type เป็น JSON
      data: JSON.stringify({ username: username, password: password }), // ส่งข้อมูลในรูปแบบ JSON

      success: function(response) {
        alert('Registration successful!'); // แสดงข้อความเมื่อสมัครสมาชิกสำเร็จ
        // ดำเนินการต่อ เช่น เปลี่ยนหน้า
      },
      error: function(xhr) {
        console.error(xhr.responseText); // แสดงข้อความผิดพลาดใน console
        alert('Registration failed! Please try again.'); // แสดงข้อความเมื่อสมัครสมาชิกไม่สำเร็จ
      }
    });
});


  
  