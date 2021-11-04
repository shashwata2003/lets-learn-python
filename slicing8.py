"""Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters"""
str=input()
sum=0;
cnt=0
for i in str:
    if i.isdigit():
        sum=sum+int(i)
        cnt+=1   
aveg=sum/cnt;

print(sum)
print(aveg)