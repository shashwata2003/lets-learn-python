x=int(input())
y=int(input())
l=[]
v=-1000
for i in range(x,y+1):
  u=0
  for j in range(1,i+1):
    if i%j==0:
        u+=1
  if u==2:
    l.append(i)
for i in range(len(l)-1):
  diff=l[i+1]-l[i]
  if diff>v:
    m=v
print(v)