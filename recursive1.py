def C(k):
    if k==0:
        return (0)
    if k==1:
        return(1)
    else:
        return(C(k-1)+4)

def F(n):
    if n==0:
        return (0)
    if n==1:
        return(1)
    else:
        return(F(n-1)+C(n-1))

a=int(input())
for i in range(a):
    b=int(input())
    print(F(b))

        