# x=[1,2,3,[4,5,6,[7,8,9]]]
# sum=0
# for i in x:
#     if(isinstance(i,list)):
#         for j in i:
#             if(isinstance(j,list)):
#                 for k in j:
#                     sum+=k
#             else:
#                 sum+=j
#     else:
#         sum+=i
# print(sum)
       
from functools import reduce
double=[5,7,8,9,10,1,2,9,4]
op=reduce(lambda x,y:x+y,double)
print(op)


# op=reduce(lambda x,y:x if x>y else y,double)