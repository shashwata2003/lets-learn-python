"""Given N, Find out all palindrome numbers between 1 to N
Input
50
Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44]"""
n=int(input())
a=list(range(1,n+1))
#print(a)
b=[]
for i in a:
    temp=i
    rev=0
    while i>0:
        dig=i%10
        print(dig)
        rev=rev*10+dig
        print(rev)
        i=i//10
    if (temp==rev):
        b.append(temp)
    else:
        break
print(b)

