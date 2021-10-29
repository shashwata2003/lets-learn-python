"""Sruthi has got the task to slicing the string S with N charecters and she has to find no of VOWELs in each slice. Your task   is to help Sruthi to slice the given string S with N charecters and Display no of VOWELs each slice.
Input Format
First line contains a string s with out any spaces Second line contains integer N

Constraints string length <100 N<=10

Output Format

print each slice and no of vowels line by line

Sample Input 0
welcome
Sample Output 0
welc: 1
elco: 2
lcom: 1
come: 2"""
str=input()
N=int(input())
x=0
for i in str:
    y=str[x:N:]
    if len(y)==4:
        vowel=0
        for a in y:
            if (a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
                vowel+=1
            else:
                continue
        print(y,':',vowel)
        x+=1
        N+=1
    else:
        break