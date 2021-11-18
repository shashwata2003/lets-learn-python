"""LIST2_PAT3
Left Rotation of array
Given a list of n integers and a number,d , perform d left rotations on the list. Then print the updated list as a single line of space-separated integers.
Input
The first line contains two separated integers denoting the  respective values of n (the number of integers) and d (the number of left rotations you must perform).
Output
Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.
Input
8 3
4 5 6 7 8 9 1 2
Output
7 8 9 1 2 4 5 6"""
s=input()
n,m=map(int,s.split())
# print(n)
# print(m)
L=list(map(int,input().split()))[:n]
# del L[0:3]
# print(L)
S=L[m:]+L[:m]
# print(S)
a=[str(int) for int in S]
b=" ".join(a)
print(b)
# a=" "
# c=a.join(c)
# print(c)

# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d*/
# def leftRotate(arr, d, n):
# 	for i in range(d):
# 		leftRotatebyOne(arr, n)

# # Function to left Rotate arr[] of size n by 1*/
# def leftRotatebyOne(arr, n):
# 	temp = arr[0]
# 	for i in range(n-1):
# 		arr[i] = arr[i + 1]
# 	arr[n-1] = temp
		

# # utility function to print an array */
# def printArray(arr, size):
# 	for i in range(size):
# 		print ("% d"% arr[i], end =" ")


# # Driver program to test above functions */
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2, 7)
# printArray(arr, 7)

# # This code is contributed by Shreyanshi Arun
