n=int(input())
lst=[]
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
index=0#标志位
M=['1','0','X','9','8','7','6','5','4','3','2']
for k in range(0,n):
    lst.append(list(input()))#输入ID
for i in range (0,n):
    z=0#求和
    for j in range(0,17):
        if lst[i][j] == 'X':
            z=z+10*weight[j]
        else:
            z=z+int(lst[i][j])*weight[j]
    if M[z%11] != lst[i][17]:
        print("".join(lst[i]))
        index=1
if index == 0:
    print("All passed")