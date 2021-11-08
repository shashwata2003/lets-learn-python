##printing the fabinocci series
x=[0,1]
for i in range(10):
    x.append(x[-2]+x[-1])
print(x)