"""FUNCTIONS-5
Create a Tic Tac Toe program with the following rules USING FUNCTIONS

Given the board configuration of the tic tac toe game, determine if the board is in either of the following states: empty, player1 wins, player2 wins, draw or intermediate. The board is said to be in initial state if all the cells contain ‘-1’, player1 uses ‘1’ as his coin and player2 uses ‘2’ as his coin. The game is draw when the board is full and no one has won the game.  The game is in intermediate state when no one has won and board is not full

Represent the board in memory
Get the elements in first row, second row and so on
Process the elements
If all are -1 then print ‘empty’
If ‘1’ is placed row wise, column wise or diagonally then print ‘Player 1’ wins
If ‘2’ is placed row wise, column wise or diagonally then print ‘Player 2’ wins
If all cells are full and no one has won the game then print ‘Draw’
Otherwise print intermediate
INPUT;j

1 -1 2

-1 1 2

2 -1 1

OUTPUT

player 1 wins"""
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