"""string1
In a college students are playing a game in their activity class.they are given cards with words on them and then the students have to sort them alphabetic order.Suma is a student in that class who is good in python programming. She want to write a python program for this task your task is to help her.
Given S is a line of string with multiple words.Suma and you have to read the line of string and sort the words in alphabetic order display them with lenth of each word.
Input Format
single line of string
Constraints
lenth of string>0
Output Format
print sorted words line by line with lengths
Sample Input 0
hello this is an example with cased letters
Sample Output 0
The sorted words are:
an : 2
cased : 5
example : 7
hello : 5
is : 2
letters : 7
this : 4
with : 4"""
a=list(input().split())
# print(a)
b=sorted(a)
# print(b)
print('The sorted words are:')
for i in b:
    x=len(i)
    print(i,':',x)