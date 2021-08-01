n=int(input())
graph=[]
for i in range(n):
    graph.append(eval(input()))
print(graph)
num_vertex=len(graph)
num_edge=0
num_weight=0
for ifmtion in graph:
    dic=ifmtion[list(ifmtion.keys())[0]]
    num_edge+=len(list(dic.values()))
    num_weight+=sum(list(dic.values()))
print(f"{num_vertex} {num_edge} {num_weight}") 