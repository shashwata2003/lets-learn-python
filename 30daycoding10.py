"""Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.
Example
The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .
Input Format
A single integer, .
Constraints
Output Format
Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .
Sample Input 1
5
Sample Output 1
1
Sample Input 2
13
Sample Output 2
2
Explanation
Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .
Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is ."""   
# n=int(input())
# while (True):
#     if n>=1:
#         n=n//2
#         a=n%2
#         print(a) 
# Function to convert decimal number
# to binary using recursion
num = int(input())

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    num //= 2

print(maximum)