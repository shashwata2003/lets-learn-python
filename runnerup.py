"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up."""
n = int(input())
arr = map(int, input().split())
L=set(arr)
a=list(L)
# print(a)\
b=sorted(a)

print(b[-2])

# a=sorted(L)

# for i in range(0,n):
#     print(i)
#     if a[i]==a[i+1]:
#         b=4
#     else:
#         b=3
#         continue

# print(a[b])
# # print(L)
# # print(a)

