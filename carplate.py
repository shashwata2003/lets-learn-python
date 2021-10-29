"""Rajesh bought a new car and he is interested to get a fancy number for his car. According to Rajesh,  A number is considered fancy if its digits sum up to exactly 10. Write a program that checks whether Rajesh can choose the given number. Note : Car registration number does not exceed 4 digits.

Input

1234

Output

Fancy

Input

123

Output

Not Valid

Input

2345

Output

Not Fancy"""
a,b,c,d=input().split()
x=a+b+c+d
if x==10:
    print("Fancy")
elif x<10:
    print("Not Fancy")
elif x>10:
    print("Not Fancy")
else:
    print("Not Valid")