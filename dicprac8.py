n=int(input())
d1={}
d2={}
for i in range(n):
    a_one=input()
    b_one=a_one.split()
    b_one[1]=int(b_one[1])
    d1[b_one[0]]=b_one[1]
for f in range(n):
    c_one=input()
    d=c_one.split()
    d[1]=int(d[1])
    d2[d[0]]=d[1]
# print(d1)
# print(d2)

# for g in d2.keys():
#     # print(g)
#     x=d1[g]+d2[g]

print(d1['a'])
print(d2['a'])
print(d1['b'])
print(d2['b'])
print(d1['c'])
print(d2['c'])
    