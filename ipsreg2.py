"""Assume that you are entering a shopping mall with your car. You need to pay for parking vehicle. An operator was doing manual calculation for calculating the total hours spent. Help him do it automatically by writing a python code. Also mall opens by 8AM in the morning and clases by 12 in the night. No cars can be parked after 12.
Upto 3 hours Rs.100
for every additional hour :Rs.40
Input
Intime in the 24 hrs format 
outtime in 24 hrs format
Output
Amount in Rs
Input 
10:00
22:20
Output
Rs.500
Input 
10AM
10:20 PM
Output
Invalid Input"""
import re


n=input()
m=input()
# print(n[0])
cost=0
if re.match('[0-9]{2}:[0-9]{2}$',n) and re.match('[0-9]{2}:[0-9]{2}',m):
    a=int(n[0])#*10)#+n[1]
    b=int(m[0])#*10)#+m[1]
    e=int(n[1])
    f=int(m[1])
    g=int(n[3])
    i=int(m[3])
    j=int(n[4])
    k=int(m[4])
    c=a*10+e ##hour of entry
    d=b*10+f ## hour of leaving
    l=g*10+j ##min of entry
    p=i*10+k ##min of exit
    o=d-c ## total hours 
    q=p-l ## extra min
    if o>3:
        if q>0:
            r=o-3
            s=r*40
            cost=100+s+40
        print('Rs.',cost,sep='')
    else:
        cost=100
        print('Rs.',cost,sep='')
else:
    print('Invalid Input')
