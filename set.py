"""find the no. of student who failed in one or more subjects"""
"""SET ALWAYS IGNOES THE EPETAED VALUES IN THE INPUT"""
# x={1,2,3,4}##is the set of elem
# x1=set('shashwata')
# print(x1)##set doesnot take any repeatations
# x1.add('alot')##adding elements
# print(x1)
# s1={1,2,3,4}
# s2={1,2,3,4}
# print(s1|s2)##union function of sets 
# print(s1&s2)##intersection function
# print(s1-s2)##removed the elements of s2 from s1
# print(s1<s2)##checks if s1 is a subset of s2
# set()##empty set
# L=[1,2,34,3]
# A=set(L)##converted to set
# print((10,20) in s1)
# s3=s1.copy()
# print(s3)
# s1.difference_update(s2)##here the s1 value change wheresas in case of x-y which have the same function but it use to change the the value of xz
# print(s1<s2)##check if all the elemt are present in s1 of s2
# print(s1<=s2)##checks for sebset not proper subset 
# a={x**2 for x in [1,2,3,4]}
# print(a)
"""******************************************"""
n=int(input())
s=set(map(int,input().split()))
m=0
h={m+i for i in s}
print(h)