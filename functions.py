#map

# 1) Add Country Code to Phone Numbers Given phone numbers ["9876543210", "9123456780", "9988776655"], 
#      use map() to add +91- before each number.
#code:
# num=["9876543210", "9123456780", "9988776655"]
# op=map(lambda x:"+91 "+x,num)
# print(list(op))

# 2) Convert Prices from Dollars to Rupees
# Given product prices [10, 25, 40, 100] in dollars, use map() to convert them to 
# rupees (1 USD = 83 INR).
# code:
# rupee=[10, 25, 40, 100]
# op=map(lambda x: x*83,rupee)
# print(list(op))

# 3) Mask Credit Card Numbers From ["1234567890123456", "9876543210987654"], use map() 
#       to mask them as "******3456".
#code:
# c_num=["1234567890123456", "9876543210987654"]
# op=map(lambda x:"*"*(len(x)-4)+x[-4:] ,c_num)
# print(list(op))

# 4) Format Product Labels From ["apple", "mango", "orange"], use map() to 
# format them as → "Product: Apple".
#code:
# prd=["apple", "mango", "orange"]
# op=map(lambda x: "Product:"+x.capitalize(),prd)
# print(list(op))


# -------------------------------------------------------------------------------------------------
#filter

# 1) Filter Gmail IDs From ["harish@gmail.com", "abc@yahoo.com", "xyz@gmail.com"], use filter() to 
#       keep only Gmail IDs.
#code:
# import re
# eid=["harish@gmail.com", "abc@yahoo.com", "xyz@gmail.com"]
# reg=re.compile(".+@gmail\.com$")
# op=filter(lambda x: re.search(reg,x),eid)
# print(list(op))

# 2) Get Short Product Names From ["Pen", "Notebook", "Laptop", "Charger", "Bag"], use filter()
    #   to return names with length ≤ 5.
# code:
# prd=["Pen", "Notebook", "Laptop", "Charger", "Bag"]
# op=filter(lambda x: len(x)<=5 ,prd)
# print(list(op))

# 3) Convert Names to Usernames
# From ["Harish", "Sushma", "Nandu"], use map() to convert into usernames (lowercase with @gmail.com).
#        → ["harish@gmail.com", "sushma@gmail.com", "nandu@gmail.com"]
#code:
# nm=["Harish", "Sushma", "Nandu"]
# op=map(lambda x: x.lower()+"@gmail.com",nm)
# print(list(op))

# 4) Filter Expired Products Given ,product expiry years [2022, 2023, 2025, 2026], use filter() to 
# keep only expired ones (assume current year = 2025).
# code :
# exp_date=[2022, 2023, 2025, 2026]
# op=filter(lambda x: x<2025,exp_date)
# print(list(op))

# 5) Filter High Salary EmployeesFrom [25000, 45000, 60000, 15000, 80000], use filter() 
# to return employees with salary ≥ 40,000.
#code:
# salary=[25000, 45000, 60000, 15000, 80000]
# op=filter(lambda x:x>=40000,salary)
# print(list(op))

# 6) Students Passed From student marks [35, 80, 55, 20, 90], use filter() 
# to return students who scored ≥ 40.
#code:
# marks=[35, 80, 55, 20, 90]
# op=filter(lambda x: x>=40,marks)
# print(list(op))

# 7) filter Strong Passwords From ["abc123", "Admin@123", "hello", "Pa$$word"], use filter() 
# to return only strong passwords (length ≥ 8 and must contain @ or $).
#code:
# import re
# pwd=["abc123", "Admin@123", "hello", "Pa$$word"]
# regex=r"[@ $]"
# op=filter(lambda x: len(x)>=8 and re.search(regex,x),pwd)
# print(list(op))

# 7) Process Transaction Records Given transactions 
# as ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]:
# * Use map() to extract the amounts as integers.
# * Use filter() to separate credits and debits.
#code:
import re
trn=["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]
output1=map(lambda x: x.split("-")[0],trn)
print("Amount:",list(output1))

credit=filter(lambda x:re.search("CREDIT",x),trn)
print("credit:",list(credit))
debit=filter(lambda x: re.search("DEBIT",x),trn)
print("debit:",list(debit))