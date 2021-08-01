def computeNum(l,num):
    for i in l:
        if type(i)!=list:
            co.append(num)
        else:
            computeNum(i,num-1)
    
co=[]
l=eval(input())
computeNum(l,10)
print(sum(co))