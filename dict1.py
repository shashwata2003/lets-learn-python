# """dictionary2
# XYZ organization maintains all its employee details (Eno, ename, Designation and salary) as a dictionary . XYZ wants to find
# The total salary paid every month.
# The employee details  with highest salary.
# The employee details with lowest salary.
# Write a program that helps XYZ company to achieve the same.
# Sample Input
# 12
# 1 Amit Operator 12000
# 2 Rahul Manager 120000
# 3 Mukund Head 500000
# 4 Rajesh Manager 100000
# 5 Maya Developer 45000
# 6 Mahe Designer 60000
# 7 Geetha Tester 40000
# 8 Kanch Designer 65000
# 9 Hepsi Teamlead 90000
# 10 Satosh Projectlead 110000
# 11 Raji Trainee 30000
# 12 Thilak Trainee 30000
# Output
# 1202000
# 3 Mukund Head 500000
# 1 Amit Operator 12000"""
# n=int(input())
# d={}
# for i in range(n):
#     elem=input().split()
#     elem[3]=int(elem[3])
#     d[elem[0]]=elem[1:]
# # print(d)
# s=[]
# k=[]
# for i in d.keys():
#     a=d[i][2]
#     s.append(a)
#     k.append(i)

# total=0
# high=-1
# low=9999999

# for g in d.keys():
#     total=total+d[g][2]
#     if d[g][2]>high:
#         high=d[g][2]
#         e=g
#     if d[g][2]<low:
#         low=d[g][2]
#         f=g
# print(total)
# print(e,d[e][0],d[e][1],d[e][2])
# print(f,d[f][0],d[f][1],d[f][2])
a=input().split()
print(len(a))
