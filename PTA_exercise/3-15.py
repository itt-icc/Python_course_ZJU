s=input()
a=[]
for i in s:
    if i not in a:
        a.append(i)
a.sort()
print(''.join(a))