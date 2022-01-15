"""While on his duty, a traffic police had the task of checking the speed of vehicles. It is given that if the
speed is above 90kmph, there should be a fine of 1000/- imposed on the vehicle. At the end of the
day the traffic police needs to update the number of traffic violations and total fine collected. Help
the police to implement the same using python
Testcase
Input
First line represents the number of vehicles n
The following line represent the speed of the n vehicles
Output
First line should be the number of traffic violations
Second line represents the fine collected
Input
6
95 60 100 80 85 92
Output
3
3000"""
lst = list(map(int, input().split()))
print(lst)