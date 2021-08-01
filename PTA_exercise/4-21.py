n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
point=[]
for i in range(n):#每一行
    p=max(matrix[i])#找出行中最大的
    for k in range(n):
        if matrix[i][k]==p:#如果这一行中某个元素是最大值
            min=p
            for j in range(n):
                if matrix[j][k]<=min:
                    min=matrix[j][k]
            if min==p:
                print(i,k)

                    
                
        