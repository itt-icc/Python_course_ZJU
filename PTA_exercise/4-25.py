n=int(input())
sum=0
i=1
while 2*i-1<=n:
    item=1
    for j in range(1,2*i):
        item*=j
    sum+=item
    i+=1
print(f"n={n},sum={sum}")
