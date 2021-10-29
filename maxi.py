"""3.	Write a python program to find the difference between the maximum and minimum numbers among the set of numbers entered by the user. 
Input format:
N  // no. of numbers  (If N is not greater than 1, print invalid input)
M1"""
n=int(input())
i=1
li=[]
while i<=n:
    a=int(input())
    i+=1
    li.append(a)
b=max(li)
c=min(li)
diff=b-c
print(diff)
# print(maxi)
# c=li[:1]
# int(c)
# print(c)
 