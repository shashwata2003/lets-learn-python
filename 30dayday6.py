"""Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.
Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
Note:  is considered to be an even index.
Example
Print abc def
Input Format
The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a string, .
Constraints
"""
n=int(input())
for i in range(n):
    a=input()
    b=len(a)
    l1=[]
    l2=[]
    s1=''
    s2=''
    # print(b)
    for j in range(0,b):
        if j%2==0:
            x=a[j]
            s1=s1+x
        else:
            y=a[j]
            s2=s2+y
print(s1," ",s2)
# print(s2)
# print(l1)
# print(l2)
# x=''.join(l1(m) for m in l1)
# print(x)
# for x in l1:
#     st1=''.join(x)
# print(st1)
