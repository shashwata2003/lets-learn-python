"""wRITE a PYTHON program using functions
Given the follwing details of a set  of n students
Name Enrollment number M1 CR1 M2 CR2 M3 CR3 M4 CR4 M5 CR5 M6 CR6 
Display the topper's name enrollmentno marks and GPA and the number of students who got less than 5 GPA
Input
First line represents the number of students n
Each of the following n lines has the following formar
Name Enrollmentnumber M1 CR1 M2 CR2 M3 CR3 M4 CR4 M5 CR5 M6 CR6
OUTPUT
DETAILS OF TOOPER AND GPA IN FIRST LINE
NUMBER OF STUDENTS WHO GOT LESS THAN 5 GPA IN SECOND LINE
Grades and Weightage
S- 10
A-9
B-8
C-7
D-6
E-5
F-4
GPA FORMULA=(M1*CR1)+(M2*CR2)*(M3*CR3)*(M4*CR4)*((M5*CR5)*((M6*CR6)/(CR1+CR2+CR3+CR4+CR5+CR6)
INPUT
3
RAJ 12345 10 2 9 3 8 4 10 2 10 1 10 2 
PRIYA 12346 10 2 9 3 9 4 8 2 7 1 10 2 
PREETI 12347 8 2 8 3 8 4 9 2 8 1 9 2  
OUTPUT
RAJ 12345 10 2 9 3 8 4 10 2 10 1 10 2  9.21
0"""
def GPA(a):
    a[1]=int(a[1])
    a[2]=int(a[2])
    a[3]=int(a[3])
    a[4]=int(a[4])
    a[5]=int(a[5])
    a[6]=int(a[6])
    a[7]=int(a[7])
    a[8]=int(a[8])
    a[9]=int(a[9])
    a[10]=int(a[10])
    a[11]=int(a[11])
    a[12]=int(a[12])
    a[13]=int(a[13])
    b=float((a[2]*a[3])+((a[4]*a[5])*(a[6]*a[7])*(a[8]*a[9])*(a[10]*a[11])*(a[12]*a[13]))/(a[3]+a[5]+a[7]+a[9]+a[11]+a[13]))
    return b
c=input().split()
d=GPA(c)
print(d)    