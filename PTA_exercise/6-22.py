def prime(p):
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
def PrimeSum(m,n):
    sum=0
    if m ==1:m=2
    for i in range(m,n+1):
        if prime(i):sum+=i
    return sum
m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))