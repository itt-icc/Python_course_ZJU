n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
sum=0
for i in range(n-1):
    for j in range(n-1):
        if i+j==n-1:
            continue
        else:
            sum+=matrix[i][j]
print(sum)