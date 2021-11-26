"""DICTIONARY1
Assume that you are given the details of n students  (regno,name,Eng Marks, Math marks, Python marks, Chem marks, Phy marks). Find out the register number, name and average of the overall topper (Use Dictionary)
Sample Input
4
BCE1001 Mahi 90 78 67 84 79
BRS1082 Rathi 90 93 94 98 96
BRS1011 Ranjan 80 87 67 23 80
BRS1900 Kathir 90 87 86 81 78

Sample output
BRS1082 Rathi 94.20"""
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
# print(d)
gret=-1
for j in d.keys():
    c=(d[j][1]+d[j][2]+d[j][3]+d[j][4]+d[j][5])/5
    if c>gret:
        gret=c
        x=j
        temp=c
print(x,d[x][0],'%.2f'%temp)        
    