n=list(map(int,input().split(',')))
second=[6,7,8,9,10]
a=[]
for i in second:
    if i not in n:
        a.append(i)
print(*a,sep=' ')