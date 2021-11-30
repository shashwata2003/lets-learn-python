"""Sruthi has got the task to slicing the string S with N charecters and she has to find no of VOWELs in each slice. Your task is to help Sruthi to slice the given string S with N charecters and Display no of VOWELs each slice.
Input Format
First line contains a string s with out any spaces Second line contains integer N
Constraints
string length <100
N<=10
Output Format
print each slice and no of vowels line by line
Sample Input 0
welcome
4
Sample Output 0
welc: 1
elco: 2
lcom: 1
come: 2"""
a=input()
n=int(input())
x=0
temp=0
for i in range(n):
    b=a[x:n]
    x=x+1
    n=n+1
    y=0
    # print(b)
    for j in b:
        if (j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u'):
            y+=1 
            
        else:
            continue   
    print(b,':',' ',y,sep="")
