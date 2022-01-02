"""Pakya and Jani started to play a new game. The game contains a board which consists of concentric circles. When Pakya correctly hits the center of the concentric circles, her score is equal to target score. The score gets reduced depending on where the players hit on the board. When the players hits outside the board, his score is 0. Each player is given exactly 5 turns. Each player plays all 5 turns. Score gets accumulated after every turn.

Can you write a program to determine the minimum number of turns  pakya and Jani takes to reach the target score of ‘n’

Input Format:

Input consists of 3 lines. The first line corresponds to the target score 'n'.

Second line  consists of scores of Pakya for each turn

And Third line  consists of scores of Jani for each turn

Output Format:

Output consists of  minimum turns taken by Pakya and Jani to meet target 0 otherwise
Sample Input and Output1:

100

20 30 50 40 100

70 60 100 20 100

Output

3

2

 

Sample Input and Output1:


200

20 30 50 40 30

70 60 100 20 100

Output

0

3"""
def score(n):
    for i in range(2):
        sum=0
        c=0
        a=input().split()
        if len(a)==5:
            a[0]=int(a[0])
            a[1]=int(a[1])
            a[2]=int(a[2])
            a[3]=int(a[3])
            a[4]=int(a[4])
            for  j in range(0,4):
                if sum<n:
                    sum=sum+a[j]
                    if sum>=n:
                        print(c+1)
                        break
                    # if sum!=n:
                    #     print('0')
                        
                    else:
                        c=c+1
                elif sum!=0:
                    print('0')
                    
            # else:
        # else:
        #     print('0')    #     print('0')
    

n=int(input())
score(n)
                