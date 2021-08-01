def permutations(arr, position, end):
    if position<end:
        for index in range(position, end):
            print(index,position,arr)
            arr[index], arr[position] = arr[position], arr[index]#当前位置可以和自身以及身后的元素交换
            permutations(arr, position+1, end)#下一个位置继续交换
            arr[index], arr[position] = arr[position], arr[index]#恢复原来样子
    elif position == end:#如果指针指到最后一个位置，最后情况
        l.append(int("".join(arr)))
n = int(input())
arr=[]
for i in range(1,n+1):
    arr.append(str(i))
l=[]
permutations(arr, 0, len(arr))
l.sort()
print(*l,sep="\n")