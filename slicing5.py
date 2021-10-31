"""Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first."""
x=input()
up=[]
low=[]
for i  in x:
    if i.isupper():
        up.append(i)
    else:
        low.append(i)
a=''.join(up + low)

print(a)
