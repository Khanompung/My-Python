Weight =float(input("น้ำหนัก"))
Height =float(input("ส่วนสูง"))
BMI = round (Weight/(Height/100)**2,2)
print(BMI)
if BMI < 18.50:
    print("ผอม / น้ำหนักน้อย")
elif BMI >= 18.50 and BMI <= 22.90:
    print("ปกติ / สุขภาพดี")
elif BMI >= 23 and BMI <= 24.90:
    print("ท้วม / โรคอ้วนระดับ1")
elif BMI >= 25 and BMI <= 29.90:
    print("อ้วน / โรคอ้วนระดับ2")
elif BMI >= 30:
    print("อ้วนมาก / โรคอ้วนระดับ3")


