m,n=map(int,input().split())
if n>m:
    m,n=n,m
M,N=m,n
r=m%n
while r>0:
    m,n=n,r
    r=m%n
greater=M
while greater%M!=0 or greater%N!=0:
    greater+=1
print(f"{n} {greater}") 