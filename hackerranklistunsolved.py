n=int(input())
L=[]
for i in range(n):
    a=input().split()
    if a[0]=='remove':
            a[1]=int(a[1])
            L.remove(a[1])
    if a[0]=='append':
            a[1]=int(a[1])
            L.append(a[1])
    if a[0]=='insert':
        a[1]=int(a[1])
        a[2]=int(a[2])
        L.insert(a[1],a[2])    
    if a[0]=='sort':
        L.sort()
    if a[0]=='pop':
        
        L.pop()
    if a[0]=='reverse':
        L.reverse()
    elif a[0]=='print':
        print(L)
