x='shashwata'
a=list(x)
print(list(x))
print(list(range(10)))
print(x[3])
print(x[-2])
print(x[0::2])
y=[1,2.3,7.5,8,6,1.03]
z=[1,2,3,4,5,5,6,5]
print(sum(y))
print(max(y))
print(min(y))
print(sorted(y)) ##Ascending order
print(sorted(y,reverse=True)) ##Decending order
print(sorted(y,reverse=False)) ##Ascending order
print(sorted(x)) ## Ascending alpabatically
print(sorted(x,reverse=True))##Decending alpabatically
print(z+y)
print(a.index('a'))
print(y.index(max(y)))
y.reverse() ##this reverse command need to be initiated first then printed
print(y)
y.append(13) ## Append function only takes one value
print (y)
y.pop(2)##removing by the position of the variable
print(y)
y.remove(7.5)## removing by item
print(y)
del y[1:4]##deleting the entire segment
print(y)
a.insert(2,'a')##entering a element in the list a.insert(position,text that needed to be added)
print(a)
print(z.count(5))##counting the repeated numbers
print(a.count('a'))
##Creating a list 
x=range(1,20,2)
y=list (x)
print(y)
p=list(range(2*10+5))
print(p)