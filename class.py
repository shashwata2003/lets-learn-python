
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return (n%10) + sum(n//10)
# x=sum(23334)
# print(x)
def dic(n):
    d={}
    for i in range(n):
        a=input().split()
        a[1]=int(a[1])
        d[a[0]]=a[1:]
    return d
n=int(input())
x=dic(n)
print(x)

    