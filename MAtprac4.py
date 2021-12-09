"""An ISBN number is legal if it consists of 10 digits and d_1 + 2d_2 + 3d_3 + ... + 10d_10 is a multiple of 11. The ISBN number 0-201-31452-5 is valid. 15 + 22 + 35 + 44 + 51 + 63 + 71 + 80 + 92 + 10*0 = 88 and 88 is a multiple of 11."""
import re
n=input()
x=len(n)
# print(x)
sum=0
count=1
if re.match('[0-9]{10}',n):
    for i in range(0,x):
        a=count*int(n[i])
        sum=sum+a
    if sum%11==0:
        print('yes')