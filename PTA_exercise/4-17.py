# n=int(input())
# m=list(range(1,n+1))
# i=1
# count=0
# while len(m)>1:
#     if i%3==0:
#         print(i)
#         print(len(m))
#         m.remove(m[(i-1)%(len(m))])
#         count+=1
#         print(m)
#     i+=1
#
def king(m, n):
    lt = list(range(1, m+1))
    i = 0
    while len(lt) > 1:
        monkey = lt.pop(0)
        i += 1
        # 判断计数是否等于要剔除的数字，如果等于，剔除已经取出的猴子
        if i == n:
            i = 0#相当于删除
        else:
        	# 将取出的第一个猴子放入列表的最后一个，形成循环
            lt.append(monkey)
    return lt[0]


m = int(input('请输入猴子的总数：')) 
n = 3
print(king(m, n))
