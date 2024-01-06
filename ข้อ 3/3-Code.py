correct_username = "admin"
correct_password = "Ad13n@23t"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("เข้าสู่ระบบไม่สำเร็จ กรุณาตรวจสอบ Username หรือ Password อีกครั้ง")