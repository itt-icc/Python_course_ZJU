def sumlist(l,level,point):#递归求嵌套和
    for i in l:
        if type(i)==int:
            if level==point:
                li.append(1)
            else:
                li.append(0)
        else:
            sumlist(i,level+1,point)
    return li
l=eval(input())
point=int(input())
li=[]
level=1
print(sum(sumlist(l,level,point)))