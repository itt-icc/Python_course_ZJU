N=int(input())
ID=[]
for i in range(N):
    ID.append(input())
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
error=[]
check='1 0 X 9 8 7 6 5 4 3 2'.split(' ')
for item in ID:
    sum=0
    item_=list(item)#列表中每个元素是字符
    wrong=0
    for j in item_[:-1]:#判断前17位是否全部为数字
        if j not in list('0123456789'):
            wrong=1
    if wrong==1:#如果不是数字
        error.append(item)
        continue
    for j,k in zip(item_[:-1],weight):#判断校验码是否正确
        sum+=int(j)*k
    if check[sum%11]!=item[-1]:#如果验证码对不上
        error.append(item)
if len(error)==0:
    print('All passed')
else:
    for i in error:
        print(i)
    