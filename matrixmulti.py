# Python code for matrix multiplication
X=[[12,23,1],[23,45,1],[1,2,3]]
Y=[[1,2,3],[2,3,4],[5,6,7]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(X)):
# i t e r a t e t h r o u g h c olumn s o f Y
    for j in range (len(Y[0])):
# i t e r a t e t h r o u g h row s o f Y
        for k in range (len (Y)) :
            result[i][j] += X[i][k]*Y[k][j]
print(result)
