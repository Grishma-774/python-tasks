import re
reg=r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
date=input("enter the date")
op=re.search(reg,date)
if(op):
    print("valid input")
else:
    print("invalid input")
