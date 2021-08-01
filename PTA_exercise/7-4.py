def sumlist(l,level):#递归求嵌套和
    for i in l:
        if type(i)==int:
            li.append(i*level)
        else:
            sumlist(i,level+1)
    return li
l=eval(input())
li=[]
level=1
print(sum(sumlist(l,level)))