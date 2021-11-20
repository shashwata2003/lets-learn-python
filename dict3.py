"""You are given a dataset of N students belonging to the same class.The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemistry, Maths, English, Hindi. Your task is find the average marks of the class for each individual subject (Use Dictionary)
Input Format
First line will contain an Integer N, denoting the number of students in the class. Each of the Next N lines will contain a string S denoting the student name, followed by five integers m1, m2, m3, m4, m5 denoting the marks scored in each subject.
Constraints
1 <= N <= 10^3 1 <= S <= 10^2 0 <= m1, m2, m3, m4, m5 <= 100
Output Format
You have to print average marks upto two decimal places for each subject followed by a space. Sample Input 0 2 arpit 100 75 40 56 53 anushka 100 100 76 100 100 Sample Output 0 100.00 87.50 58.00 78.00 76.50
Sample Input 0
2
arpit 100 75 40 56 53
anushka 100 100 76 100 100
Sample Output 0
100.00 87.50 58.00 78.00 76.50"""
n=int(input())
d={}
for i in range(0,n):
    a=input().split()
    a[1]=int(a[1])
    a[2]=int(a[2])
    a[3]=int(a[3])
    a[4]=int(a[4])
    a[5]=int(a[5])
    d[a[0]]=a[1:]


phy=0
chem=0
math=0
eng=0
hindi=0

for j in d.keys():
    phy=int(phy+d[j][0])
for k in d.keys():
    chem=int(chem+d[k][1])
for l in d.keys():
    math=int(math+d[l][2])
for m in d.keys():
    eng=int(eng+d[m][3])
for o in d.keys():
    hindi=int(hindi+d[o][4])

# print(phy,chem,math,eng,hindi)
p=phy/n
c=chem/n
m_1=math/n
e=eng/n
h=hindi/n
print('%.2f'%p,'%.2f'%c,'%.2f'%m_1,'%.2f'%e,'%.2f'%h)
