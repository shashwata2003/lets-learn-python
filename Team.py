"""  TEAM PLAYERS
  A computer programming contest requires teams of N members each. Write a program that asks for the TOTAL number of players (t) and then give the number of teams(x) and number of players leftover(y)?
  input 
  t
 N
  output 
  x
  y"""
t=int(input())
N=int(input())
x=t//N
y=t%N
print(x)
print(y)