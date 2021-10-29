"""Chaitanya has “a” candles. When Chaitanya lights up a new candle, it first burns for an hour and then it goes out. Chaitanya is smart, so he can make “b” went out candles into a new candle. As a result, this new candle can be used like any other new candle. Now Chaitanya wonders: for how many hours can his candles light up the room if he acts optimally well? Help him find this number.
Input Format
a
b
Constraints
1 ≤ a ≤ 1000 2 ≤ b ≤ 1000
Only once candles can be reused
Output
Number of hours candles can light up the room
sample input
12
5
sample output
14
sample input
12
6
sample output
14"""
a=int(input("Total number of candles chaitanya have "))
b=int(input("number of candles needed to make a new candle is "))
c=(a//b)
d=(c+a)
print(d)
