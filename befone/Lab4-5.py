#ฟังก์ชั้นหาพื้นที่สามเหลี่ยม = 1/2*ฐาน*สูง
def triangle(base,hight):
    area = 1/2*base*hight
    print("พื้นที่สามเหลี่ยม %.3f" % area)
#print("พื่นที่สามเหลีย่ม %.3f"triangle(2,3))
A = float(input("base:"))
B = float(input("hight:"))
triangle(A,B)
