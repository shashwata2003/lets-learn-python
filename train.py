"""Train Bogies
Consider a goods train with A bogies. It starts from station X to station Y via B stations. In its travel, in every ith INTERMEDIATE station where ‘i’ is ODD, it drops out C bogies and proceeds. Find with how many bogies, it will reach station Y.
Input
A
B
C
oUTPUT
REMAINING NUMBER BOGIES WHILE REACHING STATION Y"""

a=int(input())
x=int(input())
y=int(input())
c=int(input())
b=y-x
d=b//2
e=d*c
print(a-e)