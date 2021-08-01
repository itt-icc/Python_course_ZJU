n=int(input())
l=list(map(int,input().split(" ")))
result=list(map(int,input().split(" ")))
#这是选择排序
# for i in range(0,len(l)):
#     mi=i
#     for j in range(mi,len(l)):
#         if l[mi]>l[j]:
#             mi=j
#     l[i],l[mi]=l[mi],l[i]
#     rank.append(l)
flag=True
# 插入排序算法
for i in range(len(l)):
    for j in range(i,0,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
    if l==result:
        flag=False
        continue
    if not flag:
        break
    
if flag:
    print("Merge Sort")
else:
    print("Insertion Sort")
print(*l,sep=" ")