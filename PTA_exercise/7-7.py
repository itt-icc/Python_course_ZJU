n=int(input())
id_name={}
id_score={}
id_sum={}
for i in range(n):
    words=input().split()
    score=list(map(int,words[2:]))
    id_name[words[0]]=words[1]
    id_score[words[0]]=score
    id_sum[words[0]]=sum(score)
items=list(id_sum.items())
items.sort(key=lambda x:x[1])#进行排序
maxid=items[-1][0]
print(f"{id_name.get(maxid)} {maxid} {id_sum.get(maxid)}")