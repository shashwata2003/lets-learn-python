"""Given a list of integer values, find the fraction of count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions correct to 3 decimal places. 
"""
L=list(map(int,input().split()))
lent=len(L)
p,n,z=0,0,0
for i in L:
    if i==0:
        z=z+1
    elif i<0:
        n=n+1
    else:
        p=p+1
f1=float(p/lent)
print('The fraction of positive numbers are',f1)
f2=float(n/lent)
print('The fraction of negative numbers are',f2)
f3=float(z/lent)
print('The fraction of ZEro numbers are',f3)
