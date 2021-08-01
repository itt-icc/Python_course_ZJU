n=int(input())
sum=0
for i in range(1,n+2):
    denominator=1.0
    for j in range(1,i+1):
        denominator*=j
    sum+=i/denominator
print(f"{sum:.8f}")