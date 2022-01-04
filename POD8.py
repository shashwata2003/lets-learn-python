a = input((""))
if a[9]=='A':
    b=a
    usual=b.replace('A.M','')
    # print(usual)
if a[9]=='P':
    x=int(a[0])
    y=int(a[1])
    z=str((x*10+y)+12)
    # print(z)
    b=a.replace(a[:2],z)
    usual=b.replace('P.M','')
    # print(usual)
if a[9]=='m':
    b=a.replace(a[:2],'00')
    usual=b.replace('midnight','')
    # print(usual)
heaven = ""
k = int(usual[0:2])
if(usual == "00:00:00 "):
    heaven = "08:00:00 midnight"
elif(usual == "08:00:00"):
    heaven = "08:00:00 midmorning"
elif(usual == "16:00:00"):
    heaven = "08:00:00 midevening"
elif(k<=7 and k>=0):
        heaven = usual + "A.M"
elif(k>=8 and k<=15):
    k = k-8
    b = "0" + str(k)
    heaven = b + usual[2:] + "B.M"
elif(k>=16 and k<=23):
    k = k-16
    b = "0" + str(k)
    heaven = b + usual[2:] + "C.M"

# print(usual)
print(heaven)