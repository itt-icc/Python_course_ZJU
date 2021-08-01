m=int(input())
for i in range(m):
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    flag=True
    for i in range(1,n):
        for j in range(0,i):
            if matrix[i][j]!=0:
                flag=False
                break
        if flag==0:
            break
    if flag:
        print("YES")
    else:
        print("NO")
