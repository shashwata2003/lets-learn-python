"""In a supermarket there are two sections S1 and S2. The sales details of item1 to item n of section1 and item1 to itemp of section2 are maintained in a sorted order. Write a program to merge the elements of the two sorted lists to form the consolidated list.
"""

L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
print(L2)
len1=len(L1)
len2=len(L2)
fin=[]
i,j=0,0
while i<len1 and j<len2:
    if L1[i]<L2[j]:
        fin.append(L1[i])
        i=i+1
    else:
        fin.append(L2(j))
        j=j+1
print(fin)