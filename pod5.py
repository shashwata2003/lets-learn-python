w = list(input())
k = int(input())
arr = []
for i in range(len(w)):
    if (w[i]=='a' or w[i]=='e' or w[i]=='i' or w[i]=='o' or w[i]=='u'):
        arr.append(i)
sweets = 0
for i in range(len(arr)-k+1):
    beforeLetters = 0
    afterLetters = 0
    if i==0:
        beforeLetters = arr[i]+1
    else:
        beforeLetters = arr[i]-arr[i-1]
    if i==(len(arr)-k):
        afterLetters = len(w)-arr[i+k-1]
    else:
        afterLetters = arr[i+k]-arr[i+k-1]
    sweets+=(beforeLetters * afterLetters)
print(sweets)