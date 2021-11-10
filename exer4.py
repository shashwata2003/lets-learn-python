"""Triples in a List
Alice wants to find the number of triples exist in her list which summed upto Zero.
Explanation:
For Example in a list of [-1 -1 2 -2 1 1 2]
[-1 -1 2] sum is 0
[-2 1 1]  sum is 0
Output is 2
Input
-12 12 -12 3 4
Output
0"""
a=list(map(int,input().split()))
# print(a)
s=0
cout=0
i=0
while True:
    s=sum(a[i:i+3])
    # print(sum)
    if s==0:
        cout=cout+1
    i=i+1    
    if i<(len(a)-2):
        continue
    else:
        break

print(cout)