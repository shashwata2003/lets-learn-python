"""Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result"""
x=input()
y=input()
s=[]
b=x[2::]
c=y[::-1]
d=c[2::]
a=x[0]+y[-1]+x[1]+y[-2]+b+c
print(a)
