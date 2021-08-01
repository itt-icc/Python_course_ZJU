def judge(i):
    isprime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            isprime=False
            break
    return isprime
N=int(input())
for i in range(N):
    item=int(input())
    if judge(item):
        print("Yes")
    else:
        print("No")