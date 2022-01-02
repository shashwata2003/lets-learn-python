n=input().split(" ")
b=input().split(" ")
c=input().split(" ")

L=list()

L.append(n)
L.append(b)
L.append(c)

def tic(a):
    if  L[0][0]==L[1][0]==L[2][0]=="1" or L[0][1]==L[1][1]==L[1][2]=="1" or L[0][2]==L[1][2]==L[2][2]=="1" or L[0][0]==L[1][1]==L[2][2]=="1" or L[0][2]==L[1][1]==L[2][0]=="1":
            print("player 1 wins")
    elif L[0][0]==L[1][0]==L[2][0]=="2" or L[0][1]==L[1][1]==L[1][2]=="2" or   L[0][2]==L[1][2]==L[2][2]=="2" or L[0][0]==L[1][1]==L[2][2]=="2" or L[0][2]==L[1][1]==L[2][0]=="2":
            print("player 2 wins")
    else:
        print("Intermediate")
    

tic(L)