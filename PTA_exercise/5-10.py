l=list(map(int,input().split(',')))
s=int(input())
n=len(l)
dic={}
for i in l:
    dic[i]=l.index(i)#建立字典
flag=True
for i in dic:
    if (s-i) in dic:
        print(f"{dic[i]} {dic[s-i]}")
        flag=False
        break
if flag:
    print("no answer")
