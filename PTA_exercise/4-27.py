matrix=list(map(int,input().split()))
m=[]
count=0
n=[]
for i in matrix:
    n.append(i)
    count+=1
    if count%3==0:
        m.append(n)
        n=[]
for i in range(0,3):
    for j in range(0,i):
        m[i][j],m[j][i]=m[j][i],m[i][j]
for i in m:
    for j in i:
        print(f"{j:4d}",end='')
    print()