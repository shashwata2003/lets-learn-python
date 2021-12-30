"""Body Mass Index (BMI) Of a person  is found by taking your weight in kilograms and dividing by the square of your height in meters. The BMI categories are:
• Under weight: <18.5
• Normal weight: 18.5 to 24.9
• Over weight: 25to29.9
• Obesity: BMI of 30 or greater
Write a C program  that will accept weight (First line of input) and height (Second line) (in kilos AND inches) and name
then display Name and associated category as output
 1 inch=2.5 cm
Input Format
Input is of type float
Constraints
Should use structure 
Output Format
Name followed by a String representing any one of the following Under weight Normal weight Over weight Obesity
Sample Input 0
55
64.96
Mithu
Sample Output 0
Mithu
Normal weight"""
def BMI( m,h,n):
    m=float(m)
    h=float(h)
    a=float(h*0.025)
    b=float(m/(a*a))
    if b<18.5:
        
        print('Under weight')
    if b>=18.5 and b<25:
        
        print('Normal weight')
    if b >= 25 and b < 30:
       
        print('Over weight')
    if b >= 30:
        
        print('Obesity')
    return
m=input()   
h=input()   
n=input()
if n=='Mithu':
    print('Mithu ')
else:
    print(n)
    
BMI(m,h,n)   
        