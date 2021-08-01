# 字典合并-简化版
# Author: cnRick
# Time  : 2020-4-10
dict1 = eval(input())
dict2 = eval(input())
for key in dict2.keys():
    dict1[key] = dict1.get(key,0) + dict2[key]#r如果不存在就返回零

items_list = list(dict1.items())#字典转换成元组会多出空格来

print(items_list)

items_list.sort( key = lambda item : ord(item[0]) if type(item[0]) == str else item[0])

print(str(dict(items_list)))#含有多出的空格

print(str(dict(items_list)).replace(" ","").replace("'",'"'))#对字符串进行替换操作