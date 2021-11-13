"""Watson gives Sherlock an list of N numbers. Then he asks him to determine if there exists an element in the list such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
""" 
L1=list(map(int,input().split()))
a=sum(L1)
count=0
for i in L1:
    if 2*count==a-L1[i]:
        print('Yes')
    else:
        print('No')
    count=+1
        


