"""Sunny and Johnny together have M dollars they want to spend on ice cream. The parlor offers N flavors, and they want to choose two flavors so that they end up spending the whole amount.
You are given the cost of these flavors. The cost of the ith flavor is denoted by ci. You have to display the indices of the two flavors whose sum is M."""
from ast import Index


L=list(map(int,input().split()))
M=int(input())
for i in L:
    a=M-i
    if L.index(a):
        b=L.index(a)
        print(i,L[b])
        # print(L[b])
    else:
        continue