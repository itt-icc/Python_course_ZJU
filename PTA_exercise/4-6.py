n=int(input())

if(n<1):print("Invalid.")
elif n==1:Fibo=[1]
else:
    Fibo=[1,1]
    a,b=1,1
    for i in range(2,n):
        c=a+b
        a,b=b,c
        Fibo.append(c)
#输出
if n>=1:
    flag=0
    for i in Fibo:
        print(f"{i:11d}",end='')
        flag+=1
        if flag%5==0:
            print()
