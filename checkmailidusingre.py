import re
s=input()
if re.match('([A-Za-z0-9]*@[A-Za-z]*\.com|in)$',s):
    print('yes')
else:
    print('no')
