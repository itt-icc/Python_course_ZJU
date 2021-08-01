a=open("example.txt","r")
re=a.read()#读取所有内容

l=[]
for i in re:
    k=i
    if i.islower():k=i.upper()
    elif i.isupper():k=i.lower()
    l.append(k)

a.close()
b=open("result.txt","w")
b.write("".join(l))
b.close()