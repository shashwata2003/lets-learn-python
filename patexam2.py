"""LIST1_PAT3
Given a group of j numbers S = s1, s2, ..., sj and another group of k numbers Q = q1, q2, ..., qk. If (q1 + q2 + ... + qk)/k < (s1 + s2 + ... + sj)/j please print the sequence S and otherwise please print the sequence Q.
Input Format
In the first line you are given one integer 2<=n<=1000, and in the following line n integers: -1000 <= si <= 1000.
In the third line you are given one integer 2<=m<=1000, and in the following line m integers: -1000 <= qi <= 1000.
Constraints
-1000 <= si <= 1000. -1000 <= qi <= 1000.
Output Format
The sequence of requested integers separated by spaces in the same order as in the input.
Sample Input 0
5
-2 -1 0 1 4
6
-3 -2 -1 1 2 3"""
j=int(input())
n=input()
S=list(map(int,n.split()))
k=int(input())
m=input()
Q=list(map(int,m.split()))
a=sum(S)/j
b=sum(Q)/k
if b<a:
    print(S)
else:
    print(m)
    