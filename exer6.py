"""Given N, Find out all palindrome numbers between 1 to N
Input
50
Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44]"""
n=int(input())
L=list(range(1,n+1))
Out=[]

for i in L:
    temp = i
    b=i%10
    c=i//10
    rev=b*10+c
    # print(rev)
    if (temp==rev or c==0):
        Out.append(temp)
    else:
        continue
print(Out)
