import re
# # if re.match('f.o','foooo'):
# #     print("ndbsjf") ##prints the output
# # if re.match('f.o$','fooooo'):
# #     print('shgja') ## out is no as the not excatly as the f.o
if re.match('^sjhd','sjhd jdhsf'):
    print('dsffa')
#     s=input()
# # if re.match('[A-Z][a-z]',s):
# #     print('dsffa')
# if re.match('[0-9]{3}',s):
#     print('dsffa')
# # if re.match('^sjhd','sjhd jdhsf'):
# #     print('dsffa')
s=input().split('/')
if re.match('[0-9]{2}[0-9]{2}[0-9]{4}',s):
    print('yes')
