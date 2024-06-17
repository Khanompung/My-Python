print("คะแนน")
S = int(input("คะแนนของคุณ:"))
if S >= 80 and S <= 100:
    print("เกรด A")
elif S >= 70 and S <= 79:
    print("เกรด B")
elif S >= 60 and S <= 69:
    print("เกรด C")
elif S >= 50 and S <= 59:
    print("เกรด D")
elif S >= 0 and S <= 49:
    print("เกรด F")
else:
    print("กรุณากรอกข้อมูลใหม่ให้ถูกต้อง 0-100")