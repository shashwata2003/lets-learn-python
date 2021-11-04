"""Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter."""

s1=input()
s2=input()
res='true'
for i in s1:
    if i in s2:
       res='true'
        
    else:
        res='false'
print(res)
