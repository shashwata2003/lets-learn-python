"""Aravind decided to visit his friend. It turned out that the Aravind house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the Aravind can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house
Sample Input 0 : 5
Sample Output 0 :  1
Sample Input 1 : 10
Sample Output 1 : 2"""
x = int(input("Enter the location of the friends house "))
# if x <= 5 : print("1")
y = x%5
Q=x//5
if y<5 and y!=0 :print(Q+1) 
else: print(Q)