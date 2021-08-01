n=int(input())
numerator=2
denominator=1
sum=0
for i in range(n):
    sum+=1.0*numerator/denominator
    temp=denominator
    denominator=numerator
    numerator=numerator+temp
print(f"{sum:.2f}")