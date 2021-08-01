def inzi(n):
    l=[1]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            l.append(i)
            if n!=i**2:
                l.append(int(n/i))
    l.sort()
    return l

m,n=map(int,input().split())
for i in range(m,n+1):
    if i == sum(inzi(i)):
        print(f"{i} = ",end="")
        print(*inzi(i),sep=" + ")