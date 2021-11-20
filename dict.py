A=dict(name='Bob',age=40)
print(A)
D={k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
print(D)
B={x:x**2 for x in [1,2,3,4]}
print(B)
C={c.lower():c+'!' for c in ['SPAM',"EGGS","SHASH"]}
print(C)
E=dict.fromkeys(['a','b','c'],0)
print(E)
#or
F={k:0 for k in zip['a','b','c']}
print(F)