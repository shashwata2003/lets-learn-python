
"""PROVIDENT FUND
Both the employer and the employee are mandated to contribute a certain percentage of the employee's salary towards the employee's pension fund. The rate is tabulated as follows:
However, the contribution is subjected to a salary ceiling of Rs.20,000. In other words, if an employee earns Rs.60000 only Rs.20000 attracts employee's and employer's contributions, the remaining Rs.40000 does not. Given the employees age and  monthly salary, find out the total contribution made by employer and employee together per year.

Input
Salary in the first line
Age in the second line

Ouput

TOTAL CONTRIBUTION MUST ALSO BE AN INTEGER

SAMPLE INPUT

100000
36

SAMPLE OUTPUT

Total contribution per year 
88800"""
import math
X=int(input())
A=int(input())
if X>20000:
    S=20000
else:
    S=X
K=S/100
if A>65:
    J=K*5
    N=K*7.5

