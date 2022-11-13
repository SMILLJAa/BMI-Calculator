weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
height=int(input("ป้อนส่วนสูงของคุณ (cm):"))/100
bmi = weight/(height**2)

result="ไม่ทราบค่าชัดเจน"
if  bmi>=0 and bmi<18.0:
    result="น้ำหนักน้อย / ผอม"
elif bmi>=18.5 and bmi<=22.9:
    result="ปกติ (สุขภาพดี)"
elif bmi>=23.0 and 24.9:
    result="โรคอ้วนระดับ 1"
elif bmi>=25.0 and bmi<=29.9:
    result="โรคอ้วนระดับที่ 2"
elif bmi>30:    
    result="โรคอ้วนระดับ 3"
else :
    result="ไม่ทราบค่าที่ชัดเจน"

print("ค่า bmi = ", bmi , "อยู่ในเกณฑ์",result)
