def calculate_bmi():
   
    weight = float(input("น้ำหนักของคุณ (กิโลกรัม): "))
    height = float(input("ส่วนสูงของคุณ (เมตร): "))
    
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    
    if bmi < 18.5:
        return "ผอม / น้ำหนักน้อย"
    elif bmi < 23:
        return "ปกติ (สุขภาพดี)"
    elif bmi < 25:
        return "ท้วม / โรคอ้วนระดับ 1"
    elif bmi < 30:
        return "อ้วน / โรคอ้วนระดับ 2"
    else:
        return "อ้วนมาก / โรคอ้วนระดับ 3"


bmi = calculate_bmi()
print(f"BMI คือ {bmi:.2f}")
print(f"ระดับ BMI คือ: {interpret_bmi(bmi)}")
