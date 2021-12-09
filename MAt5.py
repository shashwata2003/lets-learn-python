"""Write a program which validates whether an ISBN number. For Ex: 1) if user inputs 8535902775 then it should print "Valid" 2) if user inputs 1843369283 then it should print "Not Valid"""""
import re
n=input()
if re.match('[0-9]{10}$',n):
    print('valid')
else:
    print('Not valid')