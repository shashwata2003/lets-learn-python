"""Write a program which takes a student's ID as input and check if the student is in CSE AI with Robotics branch or not. The student's year of admission can range from 2018 to 2021. . Matching must be case insensitive.
Input Format
The first line of input consists of an integer N, the number of students whose IDs you have to analyze. The next N lines of input contain an ID each. The IDs may or may not be valid.
Constraints
N<100
Output Format
For each ID, output on a seperate line True if the ID is of AI/Robotics and False otherwise."""
N=int(input())
i=1
while (i<=N):
    ID=input()
    x=ID[2:5]
    if x=='BRS':
        y=int(ID[0:2])
        if y>=18 and y<=21:
            print("True")
        else:
            print("False")
    else:
        print('False')
    i=i+1