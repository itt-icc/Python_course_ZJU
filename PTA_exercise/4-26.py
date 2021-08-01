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
for i in m:
    for j in i:
        print(f"{j:4d}",end="")
    print(f"{max(i):4d}{sum(i):4d}")