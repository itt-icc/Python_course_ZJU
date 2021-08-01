error=float(input())
sum=0
i=1
item=1
while item>=error:
    denominator=1
    for j in range(1,i+1):
        denominator*=j
    item=1.0*i/denominator
    sum+=item
    i+=1
print(f"{sum:.6f}")