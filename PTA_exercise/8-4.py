a=open("water.txt","r")
bill=dict()#创建费用字典
for i in a.readlines():
    l=i.split()
    if l==[]:continue#如果空列表就跳过
    bill[l[0]]=round((int(l[-1])-int(l[1]))*1.05,2)
a.close()
#打印账单
print("   账号   ： 费用  ")
for i in bill.items():
    print(i[0]+":"+str(i[1])+'￥')