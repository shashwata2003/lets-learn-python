"""A binary number is written as combination of 1's and 0's. Binary number 100 indicates Write a program which accepts a number and prints whether it is binary or not."""
import re
n=input()
yes=0
no=0
for i in n:
    if i=='1' or i =='0':
        # print('Yes')
        yes=yes+1
    else:
        # print('No')
        no=no+1
if no>0:
    print('no')
else:
    print('Yes')