"""In a supermarket there are two sections S1 and S2. The sales details of
item1 to itemn of section1 and item1 to itemp of section2 are maintained
in a sorted order. Write a program to merge the elements of the two
sorted lists to form the consolidated list."""

L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
L3=list(L1+L2)
print(L3)
L4=sorted(L3)
print(L4)
