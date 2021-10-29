"""Input Format

Accept a string/Sentence and a word from the user.

Constraints

Only Characters accepted.

Output Format 
Print the total count.

Input

hello hi hi welcome

hi

Output
2"""
sent=input()
word=input()
l=len(sent)
n=sent.count(word)
print(n)