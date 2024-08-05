def calculate_points():
    print("กรุณากรอกคะแนนในหัวข้อต่างๆ")
    homework = float(input("การบ้าน : "))
    test1 = float(input("คะแนนสอบกลางภาค : "))
    test2 = float(input("คะแนนสอบปลายภาค : "))
    
    total = homework + test1 + test2
    return total

def points_measure(total):
    if total <= 50:
        return "ไม่ผ่าน"
    elif total <= 79:
        return "ผ่าน"
    elif total >= 80:
        return "ดีมาก"

total = calculate_points()

result = points_measure(total)
print("คะแนนรวม: %.2f" % total)
print("คะแนนถือว่า: %s" % result)