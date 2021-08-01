l=list(input())
a,b=input().split()
cnt=0
for i in l[::-1]:
    if i==a or i==b:
        print("{:d} {:s}".format(len(l)-cnt-1,i))
    cnt+=1