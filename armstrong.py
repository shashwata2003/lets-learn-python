"""1.	Design an algorithm and write python program  to check whether the given number is an Armstrong number of three digits or not. A number is said to be Armstrong, if the sum of the cube of the digits in a three digit number is equal to that number. Check for boundary conditions, if the value entered is outside boundary conditions then enter 'Invalid input'
     Input Format:
     A number 'n'
    Output Format:
 Print ‘Armstrong’ or ‘ Not Armstrong ‘
   Boundary Conditions:
n>=100 and <=999
Sample Test case:
       370
     Output:
      Armstrong
Test case 2:
21
Output:
Invalid Input"""

num=input()
c=len(num)
if c==3:
    sum=0
    temp=num
    while temp>0:
        digit=num%10
        d=digit**3
        sum=sum+d
        temp=num//10
    if (sum ==num):
        print("true")
    else:
        print("False")

else:
    print("Invalid input")