"""set2
Assume that you are given the details of n students  (regno,name,Living City) and list of students who registered for python course.  Your Faculty wants to conduct a physical coding contest for those who lives in Chennai. Help her to find regno of all students in ascending order
Sample Input
7
BCE1001 Mahi Delhi
BRS1082 Rathi Chennai
BRS1011 Ranjan Hyderabad
BRS1900 Kathir Chennai
BRS1901 Kavi AP
BCE1011 Mahitha UP
BCE1111 Harish Punjab

Sample output
BRS1082
BRS1900"""
n=int(input())
d={}
for i in range(n):
    a=input().split()
    d[a[0]]=a[1:]
for j in d.keys():
    if d[j][1]=='Chennai':
        print(j)
