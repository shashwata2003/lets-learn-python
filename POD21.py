import math
a=int(input())

b=list(input().split())

# print(b)
for i in range(0,a):
    b[i]=int(b[i])
# print(b)
if  math.gcd(*b)>1:
    print('YES')
else:
    print('NO')
# print(math.gcd(*b))