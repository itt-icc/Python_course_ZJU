a=open("freedom.txt","r")
strs=a.read()#读取所有内容
a.close()
#创建集合
non=set()
for i in strs:
    if not i.isalpha() and i!="-":#有连字符算一个单词
        non.add(i)
for i in non:
    strs=strs.replace(i,' ')
#单词分割列表
strs=strs.rstrip(' ').lower().split()
count=dict()
for i in strs:
    count[i]=count.get(i,0)+1
ans=sorted(count.items(),key=lambda x: x[0])
b=open("dic.txt","w")
for i in ans:
    s=i[0]+":"+str(i[1])+"\n"
    b.writelines(s)
b.close()