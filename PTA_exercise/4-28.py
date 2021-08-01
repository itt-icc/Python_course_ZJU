m=list(map(int,input().split()))
n=list(map(int,input().split()))
l=[]
for i in m:
    if i not in n and (i not in l):
        l.append(i)
for i in n:
    if (i not in m) and (i not in l):
        l.append(i)
print(*l,sep=" ")
for i in l[1:-1]:
    print(f"{i}",end=' ')
print(f"{l[-1]}")