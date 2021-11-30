import re
s=input()
if re.match('[a-zA-Z0-9_/+/-]+@[a-zA-z]*/.com|in'):
    print('yes')
else:
    print('no')
