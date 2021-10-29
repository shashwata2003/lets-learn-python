"""Ramesh went for monthly grocery shopping. He went to market with “X” amount. His shopping bill was of “Y” amount. Ramesh has given complete “X” amount to shopkeeper to deduct his bill and ask him to return the money in minimum possible Indian currency notes. Write a programme to calculate pending money with him and Indian currency notes denomination.

Input Format

The first line contains Total amount that ramesh is having 'X'

The second line contains shopping bill 'Y
Remaining Balance is 8888
4 Note(s) of 2000
1 Note(s) of 500
1 Note(s) of 200
1 Note(s) of 100
1 Note(s) of 50
1 Note(s) of 20
1 Note(s) of 10
1 Note(s) of 5
1 Note(s) of 2
1 Note(s) of 1
"""
X=int(input())
Y=int(input())
Z=X-Y
print("Remaining Balance is",Z)
if Z>2000:
    print(Z//2000,"Note(s) of 2000")
a=Z%2000
if a>500:
    print(a//500,"Note(s) of 500")
b=a%500
if b>200:
    print(b//200,"Note(s) of 200")
c=b%200
if c>100:
    print(c//100,"Note(s) of 100")
d=c%50
if d>50:
    print(d//50,"Note(s) of 50")
e=d%50
if e>20:
    print(e//20,"Note(s) of 20")
f=e%20
if f>10:
    print(f//10,"Note(s) of 10")
g=f%10
if g>5:
    print(g//5,"Note(s) of 5")
h=g%5
if h>2:
    print(h//2,"Note(s) of 2")
i=h%2
if i>1:
    print(i//1,"Note(s) of 1")