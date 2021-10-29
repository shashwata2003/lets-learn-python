lower=int(input())
upper=int(input())
i=lower 
while i <= upper:
   
    for j in range(2,i):
        if (i%j != 0):
            break
        else:
            print(i)
        i+=1

   

# for i in range(lower,upper+1): 
#     if i >1:
#         for j in range(2,i):
#             if (i%j!=0):
#                 break
#             else:
#                 print(i)
