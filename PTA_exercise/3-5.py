number=''
s=input()
for i in s:
    if i in '0123456789':
        number+=i
if len(number)>0:
    print(int(number))
else:
    print('0')