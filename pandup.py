# 1. Tuple Packing & Unpacking
# a)Pack three fruits ("apple", "banana", "cherry") into a tuple.
# b) Unpack them into separate variables and print each one.

#code:
# a="apple","banana","cherry"
# print(a)
# x,y,z=a
# print(x)
# print(y)
# print(z)

# -------------------------------------------------

# 2. List Packing & Unpacking
# a)  Pack the numbers 1 to 5 into a list.
# b) Unpack so that the first element goes into a, the last element into c, and the remaining into
#     b using *.

#code:
# list=[1,2,3,4,5]
# print(list)
# a,*b,c=list
# print(a)
# print(b)
# print(c)

# ----------------------------------------------------------------------------------------

# 3. Swapping Values
# a) Swap two variables (x=10, y=20) using unpacking in one line.

#code:
# x=10
# y=20
# x,y=y,x
# print(x)
# print(y)

# ------------------------------------------------------------------------------------------

# 4.Given a list of student marks [95, 88, 76, 67, 89, 92], use unpacking to separate:
# 	i) topper (first value)
# 	ii) others (middle values),
# 	iii) last_student (last value).

#code:
# student=[95, 88, 76, 67, 89, 92]
# print(student)
# topper,*others,last_student=student
# print(topper)
# print(others)
# print(last_student)


