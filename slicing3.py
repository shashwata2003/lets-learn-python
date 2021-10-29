"""Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1."""
x=input()
y=input()
a=len(x)
b=a//2
c=x[0:b:]
d=x[b:]
e=c+y+d
print(e)
