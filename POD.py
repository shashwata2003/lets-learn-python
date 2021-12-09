"""Ramu makes a travel to one his office in a hilly region by his car. Given the height of his current location above sea level every few minutes after he starts the travel, write a code to check the number of up moves and down moves. First move is always up move.
For example, if 12 points are given as follows 45, 60, 82, 72, 65, 32, 53, 84, 103, 110, 89, 95 then there are 3 up moves and 2 down moves as shown below:"""
n=int(input())
L=list(input().split())[:n]
for i in range(0,n):
    L[i]=int(L[i])
# print(L)
up=0
down=0
for j in range(0,n-1):
    if  L[j]>L[j+1]:
        down=j
        break
# print(down)
for k in range(0,n-1):
    if  L[k]<L[k+1]:
        up=k
        break
print(down,up)