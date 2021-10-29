"""Disneyland offers a credit card to all the players playing this card game. This credit card is credited with points based on this card game - III. Patrick started to play a card game - III. In this game, he has to pick the cards which are shuffled on the table until he picks the card with the number -999. Once he picks the card with number -999, Patrick must handover all the cards picked to Disneyland card game manager. The sum of all numbers in the card is credited as points to Patrick. The players can pick any number of cards until the card with number -999 is encountered. So it is difficult for the Disneyland managers to sum up all card numbers. They approach you and ask for your help. Can you please help them with the program to sum all numbers in the card (exclude -999 when calculating the sum)?
3
4
5
-2
-999
The credit points is 10"""


sum=0
while True:
    a=int(input())
    if  a ==-999:
        break
    else:
        sum=sum+a
   
print(sum)