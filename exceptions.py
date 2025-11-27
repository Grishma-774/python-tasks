# 1.Syntax Error Check
# Write a small code snippet that will produce a compile-time (syntax) error. Then fix it.
# Example: Missing colon in an if statement.
#code:
# try:
#     x=10
#     if(x>5):
#         print("greater")
# except SyntaxError:
#     print("missing colon in if statement")

# 2.ZeroDivisionError
# Take two numbers from the user and perform division. Handle the case when the denominator is 0.
#code:
# try:
#     x=int(input("enter x:"))
#     y=int(input("enter y:"))
#     print(int(x/y))
# except ZeroDivisionError:
#     print("cant be divided with zero")

# 3.ValueError
# Ask the user for their age. Handle the case when the user enters a string instead of a number.
#code:
# try:
#     age=int(input("enter your age"))
#     print(age)
# except ValueError:
#     print("please enter integer only")

# 4.TypeError
# Try adding an integer and a string together. Handle the error.
#code:
# try:
#     num1=int(input("enter a number"))
#     str=input("enter a string")
#     print(num1+str)
# except TypeError:
#     print("integer and string can't be added together")

# 5.Finally Block
# Write a program that takes an integer input. No matter what error occurs, print "Program Completed"
#  using finally.
# code:
# try:
#     a=int(input("enter a value:"))
#     if(a>10):
#         print("greater")
#     else:
#         print("smaller")
# except ValueError:
#     print("enter only integer")
# finally:
#     print("Program Completed")

# 6.Multiple Exceptions
# Ask the user for two numbers and perform division. Handle both ZeroDivisionError
#  and ValueError separately.
# code:
# try:
#     a=int(input("enter a:"))
#     b=a=int(input("enter b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("can't be divided with zero")
# except ValueError:
#     print("enter only integers")

# 7.File Handling Error
# Try to open a file named student_data.txt. If it doesn’t exist, show a proper error message.
#code:
# try:
#    x= open("student_data.txt",'r')
#    print("opened successfully")
# except FileNotFoundError:
#     print(" 'student_data.txt' does not exist in the current directory")

# 8.Catch All Exceptions
# Write a program that asks for a number and prints its square. Use Exception to handle 
# any unexpected errors.
#code:
# try:
#     x=int(input("enter a number"))
#     print(f"{x} square is {x**2}")
# except Exception:
#     print("something went wrong")

# 9.Custom Error Message
# If the user enters a negative age, raise a ValueError with a 
# custom message: "Age cannot be negative!".
#code
# try:
#     age=int(input("enter your age"))
#     if (age<0):
#         raise ValueError("Age cannot be negative!")
# except ValueError as e:
#     print(e)

# 10.Safe Calculator
# Create a simple calculator (add, subtract, multiply, divide) that takes input from the user. 
# Handle errors like invalid input, division by zero, etc.
#code:
# try:
#     num1=int(input("enter a value1"))
#     num2=int(input("enter a value2"))

#     def add(a,b):
#         return a+b

#     def sub(a,b):
#         return a-b
#     sub(num1,num2)

#     def mul(a,b):
#         return a*b
#     mul(num1,num2)

#     def div(a,b):
#         return a/b
#     div(num1,num2)

#     def cal(x,y1,y2):
#         res=x(y1,y2)
#         print(res)

#     cal(div,num1,num2)
# except ValueError:
#     print("plz enter only integer")
# except ZeroDivisionError:
#     print("can't be divide with Zero")

