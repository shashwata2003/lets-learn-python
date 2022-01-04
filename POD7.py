# import math
# def pfac(x):
#     l = []
#     for i in range(2,int(math.sqrt(x+1))):
#         if x%i == 0:
#             l.append(i)
#             if x//i !=i:
#                 l.append(x//i)
#     return sum(l)

# m = int(input())
# n = int(input())
# if(pfac(m)==pfac(n)):
#   print("No dominance")
# elif(pfac(m)>pfac(n)):
#     print(m)
# elif(pfac(m)<pfac(n)):
#     print(n)

# def factors(x):
#     for i in range(1, x + 1):
#         L=[]
#         if x % i == 0:
#             L.append(i)
#             continue
#     return L

# x=factors(360)
# y=factors(500)
# print(x,y)  
# Python Program to find the factors of a number

# # This function computes the factor of the argument passed
def print_factors(x):
       print("The factors of",x,"are:")
      L=[]
   for i in range(1, x + 1):
       if x % i == 0:
           L.append(i)
    return
        

num = 320

print_factors(num)
     
    