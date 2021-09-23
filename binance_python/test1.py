import requests
symbols = []
symbols.append("USD") # เพิ่ม index แรก คือ "USD"
symbols.append("THB") # เพิ่ม index ที่ 2 คือ "THB"

r = requests.get('https://api.fixer.io/latest?symbols='+symbols[0]+','+symbols[1]) # ดึงข้อมูล

rates = eval(r.text) # ดึงข้อมูล json ออกมาจากสตริง
symbols1 = rates['rates'][symbols[0]] # ดึงข้อมูลสกุลเงิน "USD" ออกมา
symbols2 = rates['rates'][symbols[1]] # ดึงข้อมูลสกุลเงิน "THB" ออกมา
print("Currency Converter : {} {} = {} {}".format(symbols1, symbols[0], symbols2,symbols[1])) # แสดงผล