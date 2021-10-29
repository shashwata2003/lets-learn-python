"""2.	Write a python program to print the following pattern
Input 
3
Output  (1 tab space)
1
1	2
1     2    3
"""
# rows = int(input("Enter the number of rows: "))  
  
# This will print the rows  
# for i in range(1, rows+1):  
#     # This will print number of column  
#     for j in range(1, i + 1):  
#         print(j, end=' ')  
#     print("")  
n=int(input())
i=1
while i<=n:
    i+=1
    j=1
    while j<=i:
        print(j,' ')
        j+=1
    print("")

