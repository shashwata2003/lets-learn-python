"""Sequence
Generate a sequence of numbers based othe following rules

The following iterative sequence is defined for the set of positive integers:

n → n/2(if n is even)
n → 3n + 1 (if n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Input

13

Output

13→40→20→10→5→16→8→4→2→1"""
x= int(input())

while (x != 1):
    print(x,end=' ')
    if (x%2==0):
        x=x//2
    else:
        x=(3*x+1)
print(x)


