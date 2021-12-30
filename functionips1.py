"""FUNCTIONS-1
An author "A" published a book with title "X " and ISBN number "Y". An ISBN number is legal if it consists of exactly 11 digits and the sum of the digits are divisble by 11. IF the ISBN is legal, display the message "Congratulations A, you did a great job by publishing X" otherwise display the message as "Sorry A you are blacklisted for publishing X" .
Use FUNCTIONS AND TUPLE for implementing the same
Input
3 lines
A
X
ISBN
where 
A - Author name
X title of the book
ISBN number of the book
Sample iNPUT
Kathir
Innovations for the Future
12340123402
Output
Congratulations Kathir, you did a great job by publishing Innovations for the Future"""
import re
def  ISBN(A,X,y):
    if re.match('[0-9]{11}$',y):
        sum=0
        for i in y:
            z=int(i)
            sum=sum+z
        if sum%11==0:
            print('Congratulations ',A,', you did a great job by publishing ',X,sep='')
        else:
            print('Sorry ',A,', you are blacklisted for publishing ',X,sep='')
    else:
        print('Sorry ',A,', you are blacklisted for publishing ',X,sep='')

A=input()
X=input()
y=input()
ISBN(A,X,y)
