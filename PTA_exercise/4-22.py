m,n=map(int,input().split())
flag=True
matrix=[]
for i in range(m):
    matrix.append(list(map(int,input().split())))
for i in range(1,m-1):
    for j in range(1,n-1):
        p=matrix[i][j]
        if p>matrix[i-1][j] and p>matrix[i+1][j] and p>matrix[i][j-1] and p>matrix[i][j+1]:
            print(p,i+1,j+1)
            flag=False
if flag:
    print(f"None {m} {n}")