"""FUNCTIONS-4
Find out the count and list of prime numbers between n1 and n2.
A prime number p has the divisors as 1 and p.
Input
A single line representing n1 and n2
Output
First line represents the count of prime numbers between n1 and n2
Followed by count lines  where each line has a prime number
Sample input
10 20
Output
4
11
13
17
19"""
from re import L


def prime(a,b):
    l=[]
    
    for num in range(a,b):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
           
            l.append(num)          
    return l


a,b=input().split()
a=int(a)
b=int(b)
x=prime(a,b)
# print(x)
print(len(x))
for i in x:
    print(i)
# for i in l
# prime(a,b)
