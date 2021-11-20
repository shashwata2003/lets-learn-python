"""dictionary 3
Two different e-commerce websites are selling the goods with the prices given below as array of objects such as company1 and company2. Design a program to create resultant list of products with minimum prices as shown below 
First line of input represents the number of elements m
Followed by m lines for first company
Followed by m lines for second company
Sample input
4
Product-1 100
Product-2 200
Product-3 500
Product-4 400
                                Product-1 120
                                Product-2 220
                                Product-3 300
                                Product-4 700
Sample Output
Product-1 100
Product-2 200
Product-3 300
Product-4 400"""
n=int(input())
d1={}
d2={}
for i in range(n):
        a=input().split()
        a[1]=int(a[1])
        d1[a[0]]=a[1:]
# print(d1)
for j in range(n):
        b=input().split()
        b[1]=int(b[1])
        d2[b[0]]=b[1:]
# print(d2)
for k in d1.keys():
#     print(d1[k][0])
#     print(d2[k][0])
        if (d1[k][0]>d2[k][0]):
                print(k,d2[k][0])
        else:
                print(k,d1[k][0])