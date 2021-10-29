"""Given two circles: O1 with the center o1 = (xo1, yo1) and a radius r1 and O2 with the center o2 = (xo2, yo2) and radius r2, please compute if O1 is inside O2 or if O2 is inside O1.

One line of input with 6 integers: xo1 yo1 r1 xo2 yo2 r2. 

print the following as output

print one character:
I, if O1 is inside O2 (or if O2 is inside O1),
E, if O1 is internally tangent to O2 (or if O2 is internally tangent to O1),
O, in other cases.

Input:
103 104 5 100 100 10
Output:
E"""
import math
x_1=float(input())
y_1=float(input())
r_one=float(input())
x_2=float(input())
y_2=float(input())
r_two=float(input())
pi=3.14
A_one=pi*r_one**2
A_two=pi*r_two**2

if A_one>A_two :
    print("I")
elif A_two>A_one:
    print("E")
else:
    print("O")

 