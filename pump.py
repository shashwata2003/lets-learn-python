"""Anita is driving a car which running on the low fuel. As per reading, she is left with 2.25 liter of petrol. Her car gives her mileage of 50 kilo meter per liter. She has  two options to go in Direction A or to go in direction B. She will decide on basis of petrol pump distance in either side. Help her to make this decision. Take two inputs as Distance of petrol pumps in both direction( A and B).
Input:
Enter Distance of petrol pump in direction A : 
Enter Distance of Petrol pump in direction B :
Output
A or B or NO
Input
60
90
Output
A
Input
160
90
Output 
B"""
A=int(input())
B=int(input())

if (A<B):print("A")
elif (B<A) :print("B")
else:
    print("NO")




 