n=int(input())
sum=0
for i in range(n,0,-1):
    for j in range(0,i):
        print(f"{chr(ord('A')+sum)}",end=' ')
        sum+=1
    print()