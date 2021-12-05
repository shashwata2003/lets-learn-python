n=int(input())
L=[]
for i in range(n):
    a=input().split()
    # a[1]=int(a[1])
    # a[2]=int(a[2])
    if a[0]=='insert':
        L.insert(a[1],a[2])
    if a[0]=='print':
        print(L)
    if a[0]=='remove':
        L.remove(a[1])
print(L)