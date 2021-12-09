"""Raja is hungry, he wants to find the nearest restaurant from his home. Assume Raja is residing at position (0,0) and you know the (x,y) coordinates of n restaurants. Your task is to find the nearest restaurant for Raja by writing a python code. (Loop and Math) Input: Enter Number of Restaurants3 Enter x ,y coordinates of those restaurants 2,10 2,67 2,56 Nearest restaurant is 1"""
import math
n=int(input('Enter the  no of restaurants:'))
l=[]
low=999999
for i in range(n):
    x,y=map(float,input().split())
    # x=float(input('Enter the x coordinate:'))
    # y=float(input('Enter the y coordinate:'))
    b=x*x+y*y
    c=math.sqrt(b)
    if c<low:
        low=c
        a=x
        d=y
print(a,d)
