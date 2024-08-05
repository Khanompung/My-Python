total_score = 0
score = 0
def avg(num):
    total = 0
    for i in range(num):
        score = int(input("รับคะแนน %d: " % (i + 1)))
        total += score
    average = total / num
    return average

n = int(input("จำนวนคน: "))
print("คะแนนเฉลี่ย %.2f" % avg(n))