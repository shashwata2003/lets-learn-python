"""Ramesh is running  a Marathon (N KM). He has covered  X Km in first hour. He has to finish the race in h hour . Help him to calculate on which speed per hour (z) he has run the remaining race.
Input
N
X
h
Output
z
Input
50
10
3
Output
20"""
N=int(input())
X=int(input())
h=int(input())
a=N-X
z=a//(h-1)
print(z) 