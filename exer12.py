"""Given N integers, count the number of pairs of integers whose difference is K."""
L=list(map(int,input().split()))
K=int(input())
count=0
for i in L:
    a=K-i
    if L.index(a):
        count=count+1
    else:
        continue
print(count)
    
