"""Find out the count and list of prime numbers between n1 and n2.
A prime number p has the divisors as 1 and p.
Input
A single line representing n1 and n2
Output
First line represents the count of prime numbers between n1 and n2
Followed by count lines where each line has a prime number
Sample input
10 20
Output
[4,11,13,17,19]"""

a=list(map(int,input().split()))
b=list(range(a[0],a[1]+1))
c=[]
count=0
# print(b)
for i in b:
    if i == 1:
        continue
    flag = 1
    for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break
    if (flag == 1):
         c.append(i) 
print(c)
