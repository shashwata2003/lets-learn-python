"""Dattatreya Ramchandra Kaprekar (1905–1986) was an Indian recreational mathematician who described several classes of natural numbers. He observed that any three digit number with at least two different digits gets transformed to 495 while the following steps are followed:

1) Arrange the digits of number ‘n’ in ascending and then in descending order to get two four-digit numbers, m1 and m2.
2) Compute the difference diff between m1 and m2
3) If diff is not 495 then go to Step 1.

Given a three digit number, write a code to check if the number can be transformed to 495 following above procedure. Print the number of steps for the transformation if the number can be transformed and print No otherwise."""
def reverse(n):
    a=int(n)    
    b=n[::-1]
    c=int(b)
    return a,c 
    
n=input()
# print(reverse(n))
x=reverse(n)
c=1
y=True
while y==True:
    z=x[0]-x[1]
    if z==495:
        y=False
        break
    else:
        c=c+1
        x=reverse(z)
        continue
print(c)
        






