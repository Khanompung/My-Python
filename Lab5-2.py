def mon(mo, total_vat): 
    if mo >= total_vat:
        to_mo = mo - total_vat
        return to_mo
    else:
        print("เงินไม่พอ")
        return None
def total_price(num):
    sum_price = 0
    for i in range(num):
        price = float(input("ราคาสินค้า %d: " % (i + 1)))
        sum_price += price
    return sum_price

def total_vat(sum_price, vat_rate=0.07):
    vat_amount = sum_price * vat_rate
    total_vat = sum_price + vat_amount
    return vat_amount, total_vat

n = int(input("จำนวนสินค้า: "))
sum_price = total_price(n)
vat_amount, total_vat = total_vat(sum_price)

print("ราคารวมก่อนภาษี: %.2f" % sum_price)
print("จำนวนภาษีมูลค่าเพิ่ม: %.2f" % vat_amount)
print("ราคารวมหลังภาษี: %.2f" % total_vat)
mo = float(input("จ่ายเงิน: "))
to_mo = mon(mo, total_vat)

if to_mo is not None:
    print("เงินทอน: %.2f" % to_mo)
    