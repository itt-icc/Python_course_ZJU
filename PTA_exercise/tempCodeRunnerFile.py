m,n=input().split(' ')
cnt=1
sum=0
for i in range(int(m),int(n)+1):
    if cnt%5==0 or cnt==int(n)-int(m)+1:
        print("%5d"%i)
    else:
        print("%5d"%i,end="")
    sum+=i
    cnt+=1
print("sum = %d"%sum)