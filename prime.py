num=int(input())
count=2
check=False
while (count<num):
    if ((num%count)!=0):
        count+=1
    else:
        print(num,"is not a prime number")
        check=True
    break
if check==False:
    print(num,"Is a prime number")
