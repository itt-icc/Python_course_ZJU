
def sumlist(l):#递归求嵌套和
    for i in l:
        if type(i)==int:
            li.append(i)
        elif type(i)==str:
            li.append(0)
        else:
            sumlist(i)
    return li

l=eval(input())
Sum=0
if type(l)==list or type(l)==tuple:
    for i in l:
        if type(i)==int:
            Sum+=i
        elif type(i)==list or type(i)==tuple:
            li=[]
            Sum+=sum(sumlist(i))
        elif type(i) == str:
            Sum+=0
if type(l)==int:
    Sum=l
print(Sum)
