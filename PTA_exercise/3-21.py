a=input()
b=[]
for i in a:
    if (ord(i)<=90 and ord(i)>=65) and (i not in b):
        b.append(i)
if len(b)==0:
    print("Not Found")
else:
    print(''.join(b))
