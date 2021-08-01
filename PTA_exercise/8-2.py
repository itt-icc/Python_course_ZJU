a=open("example.txt","r")
re=a.read()#读取所有内容
a.close()
dic=dict()
for i in re:
    if i.isalpha():
        dic["字母"]=dic.get("字母",0)+1
    elif i.isdigit():
        dic["数字"]=dic.get("数字",0)+1
    else:
        dic["其他字符"]=dic.get("其他字符",0)+1
print(dic)