# n=int(input())
# L=[]
# B=[]
# P=[]
# for i in range(1,n+1): 
#     if n%i==0:
#         L.append(i)
#         B.append(n//i)
# # for i in range(len(L)): 
# #     P.append(L[i],B[i])
# print(L)
# print(B)
#_______________________________________________________________________________________________________________

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
        print(li[i])
else:
    print(int((count+1)/2))
    for i in range(int((count+1)/2)):
        print(li[i])
