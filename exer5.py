"""list3
Provided S - a set of n integers S = s1, s2, ..., sn. Check whether it is possible to divide S into to parts: s1, s2, ..., si and si+1, si+2, ..., sn (1 <= i < n) 
Remember that the first part is strictly decreasing while the second is strictly increasing one.
Input Format
In the first line you are given an integer 2<=n<=100 and 
in the following line n integers
-100 <= si <= 100.
Output Format
One word Yes or No.
Input
5 
-1 2 -1 1 -1
Output
No
Input
6 
3 1 -2 -2 -1 3
Output
Yes"""
n=int(input())
a=list(map(int,input().split()))
x=sorted(a)
# print(x)
y=sorted(a,reverse=True)
# print(y)
if a == x or a==y:
    print('Yes')
else:
    print('No')