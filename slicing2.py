"""Write a program to create a new string made of the middle three characters of an input string."""
import math
st=input()
x=len(st)
y=x//2
z=math.ceil(y)
a=st[y-1:z+2:]
print(a)