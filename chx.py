n=int(input())
i=1
a=0
li=[]
posi=0
neg=0
zer=0
while i<=n:
    a=int(input())
    i+=1
    li.append(a)

for x in li:
    if (x>0):
        posi+=1
    elif (x<0):
        neg+=1
    else:
        zer+=1

print(posi)
print(neg)
print(zer)