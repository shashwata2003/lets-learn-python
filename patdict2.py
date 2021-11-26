"""Assume that you are given the details of n emplyees  (empno,name,designation,Basic pay). Find out the HRA for each employee  and find out the empno  name and HRA of the employee who earns the least HRA (Use Dictionary). HRA is calculated as 12% of the basic pay or Rs. 8000 whichever is the minimum.
Sample Input
4
1001 Mahi Manage 90000
1082 Rathi Developer 48000
1011 Ranjan Trainee 28000
1900 Kathir Designer 60000

Sample output
1011 Ranjan 3360"""
n=int(input())
d={}
for i in range(n):
    a=input().split()
    a[3]=int(a[3])
    d[a[0]]=a[1:]

leat=9999999
for j in d.keys():
    c=0.12*d[j][2]
    if c<leat:
        leat=c
        e=j
        temp=int(c)
print(e,d[e][0],temp)
    