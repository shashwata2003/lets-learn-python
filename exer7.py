"""In this pandemic, employees have been instructed to keep at least 6 feet distance from each other. Employees are lining up in a queue for food. Now, it is your duty to check whether they are all following this advice. There are a total of N spots (numbered 1 through N) where people can stand in front of the counter. The distance between adjacent spots is 1 foot. Each spot may be either empty or occupied;
you are given a list A1,A2,…,AN, where for each valid i, Ai=0 means that the i-th spot is empty, while Ai=1 means that there is a person standing at this spot. It is guaranteed that the queue is not completely empty.
For example, if N=11 and the list A is (0,1,0,0,0,0,0,1,0,0,1), then this is a queue where employees are not following the instruction because there are two persons at a distance of just 3feet from each other. You need to determine whether the employees outside the counter are following the social distancing advice or not. As long as some two people are standing at a distance smaller than 6 feet from each other, it is bad and you should report it, since social distancing is not being followed.
Display the output as YES if the reporting has to be done for not maintaining social distancing otherwise display NO
Example Input
3
3
1 0 1
7
1 0 0 0 0 0 1
11
0 1 0 0 0 0 0 1 0 0 1
Example Output
NO
YES
YES"""
n=int(input())
L=list(map(int,input().split()))[:n]
for i in L:
    if L[i]==1:
        if L[i+6]==1:
            print('NO')
            
        else:
            print('Yes')
    else:
        continue            
        
    
    


    
