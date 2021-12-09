"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""
m=int(input())  ##total no. of elem in list
n=input().split() ## input
K=int(input('Enter the toatal value of the the sum:'))
L=[]
for i in range(m):
    n[i]=int(n[i])
    L.append(n[i])

# print(L)
for i in L:
    a=K-i
    if a in L:
        print(i,'+',a,'= 17')