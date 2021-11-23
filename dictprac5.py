"""Write a function histogram() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary and print the in sorted order on 'key'.
Input Format
For each "T" test cases, we have one line:
First line contains a strings for which the frequecy of characters to be generated
1<=T<=500
1<= N<= 100
Output Format
For each of the test cases, print a dictionary that maps from frequencies to letters. For Eg.
for string S="'brontosaurus'
the program should create a dictionary
hist={'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
The dictionary 'hist' indicates that the letters ’a’ and 'b' appear once; 'o' appears twice, and so on.
sort a dict by keys and print
Letter a apperas 1 time/s
Letter b appears 1 time/s
Letter n appears 1 time/s
Letter o apperas 2 time/s
........
Letter u appears 2 time/s
Sample Input
2
abracadabra
msrit
Sample Output
Letter a  appears  5  time/s
Letter b  appears  2  time/s
Letter c  appears  1  time/s
Letter d  appears  1  time/s
Letter r  appears  2  time/s

Letter i  appears  1  time/s
Letter m  appears  1  time/s
Letter r  appears  1  time/s
Letter s  appears  1  time/s
Letter t  appears  1  time/s"""
n= int(input())
for i in range(n):
    a=input()
    b=list(a)
    
# print(b)
