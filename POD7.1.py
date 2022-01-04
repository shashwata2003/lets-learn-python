def factors(x):
    L=[]
    for i in range(1,x+1):
        if x%i==0:
            if i!=1 and i!=x:
                L.append(i)
                continue
                
    return(sum(L))
# x=factors(500)
# print(x)

x=int(input())        
y=int(input())
a=factors(x)        
b=factors(y)
if  a==b:
    print('No dominance')
elif a>b:
    print(x)
elif a<b:
    print(y)
    
    
    