"""Given a positions of coins of player1 and player2 in a 3X3 Tic Tac Toc board, write a program to determine if the board position is a solution and if so identify the winner of the game. In a Tic Tac Toc problem, if the coins in a row or column or along a diagonal is of the same player then he has won the game. Assume that player1 uses ‘1’ as his coin and player2 uses '2' as his coin. '0' in the board represent empty cell.
"""
L=[[1,2,0],[0,2,1],[1,2,0]]
for i in range(0,3):
    if(L[i][0]==1 and L[i][1]==1 and L[i][2]==1):
        print('winner 1')
        break
    elif((L[i][0]==2 and L[i][1]==2 and L[i][2]==2)):
        print('winner 2')
        break
for c in range(0,3):
    if(L[0][c]==1 and L[0][c]==1 and L[0][c]==1):
        print('winner 1')
        break
    elif(L[0][c]==1 and L[0][c]==1 and L[0][c]==1):
        print('winner 2')
        break
for c in  range(0,3):
    if(L[0][0]==1 and L[1][1]==1 and L[2][2]==1):
        print('winner 1')
        break
    elif(L[0][0]==2 and L[1][1]==2 and L[2][2]==2):
        print('winner 2')
        break

for c in  range(0,3):
    if(L[0][2]==1 and L[1][1]==1 and L[2][0]==1):
        print('winner 1')
    elif(L[0][2]==2 and L[1][1]==2 and L[2][0]==2):
        print('winner 2')

