M,N=map(int,input().split())
primelist=[]
if M<2:M=2
if N>500:N=500
for i in range(M,N+1):
    isprime=True
    for j in range(2,int(i**0.5)+1,1):
        if i%j==0:
            isprime=False
            break
    if isprime:
        primelist.append(i)
print(f"{len(primelist)} {sum(primelist)}")