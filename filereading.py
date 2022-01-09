from os import read


f=open("one.txt","wb+")
print("name",f.name)
a=f.readlines()
print(a)
print("mode",f.mode)
print(f.read())
print(f.tell())
f.close()