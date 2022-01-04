n=int(input())
count=0
li=[]
    
for i in range(1,n):
    d=int(n/i)
    if n%d==0 :
        if (n%i==0):
            count=count+1
            li.append([i,d])
            
if count%2==0:
    print(int((count/2)+1))
    for i in range(int((count/2)+1)):
        print(li[i][0],li[i][1])
else:
    print(int((count+1)/2))
    for i in range(int((count+1)/2)):
        print(li[i][0],li[i][1])
