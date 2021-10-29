"""Create a string made of the first, middle and last character"""
##taking the input
st=input()
##the last letter
y=len(st)
##the middle letter
x=int(y//2)
fin=st[0]
fin=fin+st[x]
fin=fin+st[y-1]
print("The new word formed is",fin)
