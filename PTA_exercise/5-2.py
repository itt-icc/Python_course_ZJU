n=int(input())
LGraph=[]#创建邻接表
for i in range(n):
    LGraph.append(eval(input()))
#顶点数，边数，边长度
numofvertex=len(LGraph)
numofEdge=0
weight=0
for i in LGraph:
    k=list(i.keys())
    dic=i[k[0]]#边还有权重信息
    L=list(dic.values())
    numofEdge+=len(L)
    weight+=sum(L)
print(f"{numofvertex} {numofEdge} {weight}")
    