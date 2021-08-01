def fib(n):
    result=[1,1]
    for i in range(n-1):
        result.append(result[-1]+result[-2])
    return result[-1]
def PrintFN(m,n):
    result=[1,1]
    for i in range(n):
        if result[-1]>=n:break
        result.append(result[-1]+result[-2])
    return [i for i in result if i<n and i>m]
m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))