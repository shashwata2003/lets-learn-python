dell=10
hp=100
lenovo=50
sony=4
acer=2
d={'dell':40000,'hp':42000,'lenovo':40180,'sony':39400,'acer':39300}
# print(d['dell']+d['hp'])
a=True
while a==True:
    a=input()
    b=int(input())
    if a=='Dell':
        if b<10:
            dell=dell-b
            p=b*d['dell']
        else:
            print('insufficent ')
    elif a=='HP':
        if b<100:
            hp=hp-b
            p=b*d['hp']
        else:
            print('insufficent ')
print(p)        

