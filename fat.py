"""A hostel warden needs to check the in time of students. She needs to verify whether in time is less than 8 PM. 

In time should be in 24 hrs format as below

HH:MM:SS

Use Regular expression

Input

18:45:59

Output

Yes

Input

22:35:49

Output

No

Input 

25:45:78

Output

invalid"""
import re
a=input().split(':')
# if re.match('[1-2][0-9]:[0-6][0-9]:[0-6][0-9]$,s'):
# print(a[1]+1)
if re.match('[0-2][0-9][0-6][0-9][0-6][0-9]$',a):
    a[0]=int(a[0])
    a[1]=int(a[1])
    a[2]=int(a[2])
    d=a[0]-12
    b=d*60*60+a[1]*60+a[2]
    c=8*60*60
    if b>=c:
        print('No')
    if a[0]>=24:
        print('invalid')
    else:
        print('yes')

    