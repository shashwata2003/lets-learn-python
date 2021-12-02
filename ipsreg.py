"""REG 2
MAC address is an id allocated to the computer or mobile devices at the time of manufacturing. It is used to uniquely identify a device within Local Area Network. Validate the following MAC. 
A valid MAC has 6 bytes seperated by : and each byte is presented as 2 hexadecimal numbers
Input
AB:12:cD:12:AF:CE
Output
Yes
Input
12:w0:23
Output
No"""
import re
s=input()
if re.match('[A-Za-z0-9]{2}:[A-Za-z0-9]{2}:[A-Za-z0-9]{2}:[A-Za-z0-9]{2}:[A-Za-z0-9]{2}:[A-Za-z0-9]{2}',s):
    print('Yes')
else:
    print('No')
    