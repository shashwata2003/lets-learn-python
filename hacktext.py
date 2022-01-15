a='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
b=4
c=0
for i in range(0,len(a)//b):
    c=c+b
    print(a[c:b:])
    b=b+b
    