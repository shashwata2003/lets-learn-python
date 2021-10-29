"""Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters."""
s1=input()
s2=input()

x=len(s1)
y=len(s2)
a=x//2
b=y//2
fin=s1[0]+s2[0]+s1[a]+s2[b]+s1[-1]+s2[-1]
print(fin)
