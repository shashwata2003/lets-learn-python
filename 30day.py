base=float(input())
tip=int(input())
tax=int(input())
a=float((tip/100)*base)
b=float((tax/100)*base)
total=a+base+b
c=round(total)
print(c)
