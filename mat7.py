"""Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn’t like ABAA. Given a string containing characters A and B only, he wants to change it into a string such that there are no matching adjacent characters. To do this, he is allowed to delete zero or more characters in the string. Your task is to find the minimum number of required deletions. For example, given the string S= AABAAB , remove an A at positions 0 and 3 to make S= ABAB in 2 deletions. Sample Input 5 AAAA BBBBB ABABABAB BABABA AAABBB Sample Output 3 4 0 0"""
n=int(input())
l=[]
for i in range(n):
    count=0
    a=input()
    for j in range(0,len(a)):
        if j==len(a)-1:
            break
        else:    
            if a[j]==a[j+1]:
                count=count+1
    print(count)
# n=int(input())
# l=[]
# for i in range(n):
#   b=input()
#   l.append(b)
# for i in range(len(l)):
#   a=l[i]
#   c=0
#   for j in range(len(a)):
#    if j+1<len(a):
#      if a[j]==a[j+1]:
#        c=c+1

#   print(c,)