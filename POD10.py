n=input()
a=[]
c=0
l=len(n)
val=0
for i in range(l):
    a.append(n[0:i+1])
for j in range(l):
    val=str(val)
    val=a[j]
    if(int(val)%(l-j)==0):
        c+=1
if(c==l):
    print("Yes")
else:
    print("No")