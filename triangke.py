"""Given the three angles of a triangle (x,y,z). Check whether those 3 angles can be used to form a valid triangle
Input
X
Y
Z
oUTPUT
True or False"""
x=float(input())    
y=float(input())    
z=float(input()) 
sum = x+y+y 
if x>0 and y>0 and z>0:
    if x+y>z and y+z>x and z+x>y:
        if sum ==180:
            print("True")
        else: 
            print("False")

