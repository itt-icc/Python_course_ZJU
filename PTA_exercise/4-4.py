def judge(i):
    isprime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            isprime=False
            break
    return isprime

N=int(input())
primelist=[]
if N>2000000000:N=2000000000
for i in range(2,N+1):
    if judge(i) and judge(N-i):
        print(f"{N} = {i} + {N-i}")
        break
            
