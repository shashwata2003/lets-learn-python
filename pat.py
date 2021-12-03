import re
a=2/12/2021
n=input()
if re.match('[1-9]{2}/[0-9]{2}/[0-9]{4}',n):
    b=int(n[0])
    d=int(n[1])
    e=int(n[3])
    i=int(n[4])
    j=int(n[6])
    k=int(n[7])
    l=int(n[8])
    m=int(n[9])
   
    z=int(a[0])
    o=int(a[2])
    p=int(a[3])
    q=int(a[5])
    r=int(a[6])
    s=int(a[7])
    t=int(a[8])
    
    mage=(b*10+d)+((e*10+i)*30)+((j*1000+k*100+l*10+m)*365)
    date=(n*10+o)+((p*10+q)*30)+((q*1000+r*100+s*10+t)*365)
    age=date-mage
    c=18*365
    if age>c:
        print('Yes')
    else:
        print('NO')
else:
    print('Invalid Input')