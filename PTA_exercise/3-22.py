a=input()
b=input()
flag=True
for i in a:
    if i not in b:
        flag=False
        break
if flag:
    print('yes')
else:
    print('no')