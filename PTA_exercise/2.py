height=list(map(int,input().split(' ')))
highter=[]
for i in height:
    if i>sum(height)/len(height):
        highter.append(i)
for i in highter:
    print("{} ".format(i),end='')
#print(*[i for i in height if i>sum(height)],sep=' ')