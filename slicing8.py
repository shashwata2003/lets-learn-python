import string
x=input()

for a in string.punctuation:
        newstr=x.replace(a,'#')
    
print(newstr)
