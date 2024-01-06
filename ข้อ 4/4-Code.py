weight_kg = float(input("น้ำหนัก (กิโลกรัม): "))
height_m = float(input("ส่วนสูง (เมตร): "))

bmi = weight_kg / (height_m ** 2)

print(f"BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")