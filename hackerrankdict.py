n=int(input())
d={}
for i in range(n):
    a=input().split()
    a[1]=float(a[1])
    a[2]=float(a[2])
    a[3]=float(a[3])
    d[a[0]]=a[1:]
j=input()
b=d[j][0]+d[j][1]+d[j][2]
c=b/3
print('%.2f'%c)