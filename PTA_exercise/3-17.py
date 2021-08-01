a=input()
b=[]
for i in a:
    if len(b)<10:
        if (ord(i)<=90 and ord(i)>=65) and (i.lower() not in b) and (i not in b):b.append(i)
        if (ord(i)<=122 and ord(i)>=97) and (i.upper() not in b) and (i not in b):b.append(i)
if len(b)<10:
    print('not found')
else:
    print(''.join(b))
