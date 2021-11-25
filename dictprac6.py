n=int(input())
# d={}
L1=[]
L2=[]

for i in range(1,n+1):
    L1.append(i)


d={f : f**2 for f in L1}
print(d)
