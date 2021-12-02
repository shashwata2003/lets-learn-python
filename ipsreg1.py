"""REG EX1
Check whether the given identifier is a valid SID. A valid SID has  8, 4, 4, 4, 12 hexa decimal digits separated by '-'
Input
e02fd0e4-00fd-090A-ca30-0d00a0038ba0
Output
Yes
Input
e02gd0e4-00fd-090A-ca30-0d00a0038ba0
Output
No"""
import re
s=input()
if re.match('[A-fa-f0-9]{8}-[A-fa-f0-9]{4}-[A-fa-f0-9]{4}-[A-fa-f0-9]{4}-[A-fa-f0-9]{12}',s):
    print('Yes')
else:
    print('No')