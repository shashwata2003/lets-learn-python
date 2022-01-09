import sys
sys.setrecursionlimit(1500)
def rec(k,n):
    a=0
    for i in range(1,n+1):
        if i <= 14:
            a=rec(k-1,i)+rec(k-2,i-1)
        else:
            break
    return a

b=int(input())
for i in range(b):
    k,n=map(int,input().split())
    print(rec(k,n))
    