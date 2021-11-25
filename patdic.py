
n=int(input())
d={}
for i in range(n):
    a=input()
    b=a.split()
    b[1]=int(b[1])
    b[2]=int(b[2])
    b[3]=int(b[3])
    d[b[0]]=b[1:]

high=-1
low=999999
for j in d.keys():
    m=d[j][2]/100
    bmi=d[j][1]/(m**2)
    if bmi>high:
        high=bmi
        temp=bmi
        e=j
    
print(e,d[e][0],'%.2f'%temp)