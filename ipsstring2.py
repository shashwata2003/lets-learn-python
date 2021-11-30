"""Program to Count the Occurrences of each Word in a given Sentence/String.
Input Format
Accept a string/Sentence and a word from the user.
Constraints
Only Characters accepted.
Output Format
Print the total count.
Sample Input 0
hi hi bye hi bye
bye
Sample Output 0
Count of the word is: 2"""
a=input().split()
b=input()
c=0
for i in a:
    if i==b:
        c=c+1
print('Count of the word is:',c)
