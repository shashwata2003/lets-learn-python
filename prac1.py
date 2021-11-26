"""Assume that you are given the details of n students  (regno,name,Eng Marks, Math marks, Python marks, Chem marks, Phy marks). Find out the register numbers of all students who got above 90 in maths or/and python in ascending order
Sample Input
4
BCE1001 Mahi 90 78 67 84 79
BRS1082 Rathi 90 93 94 98 96
BRS1011 Ranjan 80 97 67 23 80
BRS1900 Kathir 90 87 96 81 78

Sample output
BRS1011
BRS1082
BRS1900"""
n=int(input())
d={}
for i in range(n):
    a=input().split()
    a[2]=int(a[2])
    a[3]=int(a[3])
    a[4]=int(a[4])
    a[5]=int(a[5])
    a[6]=int(a[6])
    d[a[0]]=a[1:]
L=[]
for j in d.keys():
    if d[j][2]>=90 or d[j][3]>=90:
        L.append(j)
# print(L)
a=sorted(L)
# print(a)
for x in a:
    print(x)

            