income = float(input("กรุณาระบุรายได้ (บาท): "))

if income >= 15000 and income < 20000:
    credit_card_type = "บัตร Sliver"
elif income < 100000:
    credit_card_type = "บัตร Gold"
else:
    credit_card_type = "บัตร Platinum"

print(f"ตามรายได้ {income:.2f} บาท สามารถทำ{credit_card_type} ได้")
