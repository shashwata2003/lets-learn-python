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
y[:0]=[2,3,4] ##inserting elements at front
print(y)
y[len(y):]=[2,3,4,5]##inserting at the end 
print(y)
L=['shash','sha','ram']
L[3:]='shashwat'## used to add each character in the list 
L.append('shashw')## used to added the entire string in the list
print(L)
# print(L.sort(key=str.lower()))
## when we try to append a list it uis considered as the th element of the mother list 
L.append([1,2,3,4,5,6])
print(L)
# print(L[12[2]])
## but when we use extentent the list will be treated as each element in th elist like
L.extend([2,3,4,5,6])
print(L)
l1=list(reversed(L))
print(L)
print(l1)
L[2]=1000 ## here the secound elemet gets replaced by the new element
print(L)
L[2:]=[]## here the the lsit is replaced by empty list after 2 position
print(L)
q="".join(L) ##it si used to join two  elements of the string together
q1="-".join(L) ##it si used to join two  elements of the string together
print(q)
print(q1)
s=q.split()## coverting ito list 
print(s)
g=['1','2','3','4']

print(list (map(int,g)))##converting string to a list of integeres
r=list (map(int,input().split()))
print(r)