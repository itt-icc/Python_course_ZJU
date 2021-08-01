# import math
# a=math.sin(math.pi/180*35)+(math.exp(5)-15*5)/(5**4+1)-math.log(7*5)
# print(round(a,2))
# print("hello"'world')
# m=int(input())
# print(sum([i for i in range(11,m+1)]))
# x=int(input())
# if x==0:
#     result=0
# else:
#     result=1.0/x
# # print('f(%.1f) = %.1f'%(x,result))
# print('f({:.1f}) = {:.1f}'.format(x,result))
# x=float(input())
# if x<0:
#     print(Invalid Value!)
# elif x<=50:
#     cost=x*0.53
#     print("cost = %.2f"%cost)
# else:
#     cost=50*0.53+(x-50)*0.58
#     print("cost = %.2f"%cost)
# N=int(input())
# s=0.0
# for i in range(1,N+1,2):
#     s+=float(1.0/i)
#     print(i)
# print("sum = %.6f"%s)
# n=int(input())
# s=0.0
# for i in range(1,n+1):
#     numerator=i*1.0
#     denominator=2*i-1
#     s+=(numerator/denominator)*((-1)**(i-1))
# print("%.3f"%s)
# m=input().split(',')
# number=[]
# for i in m:
#     number.append(i.replace(' ',''))
# a,b=number[0],number[1]
# print(int(a*int(b)))
# a,b=input().replace(' ','').split(',')
# number,base=map(int,input().replace(' ','').split(','))
# transfer=0
# cnt=0
# while number>0:
#     transfer+=(number%10)*(base**cnt)
#     number=number//10
#     cnt+=1
# print(transfer)
# a=map(int,input().split(' '))
# print(list(a))
# a=map(int,input().split(' '))
# a=list(a)
# print(a)
# a=map(int,input().split(' '))
# a=list(a)
# #冒泡排序法
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# lower,upper=map(int,input().split(' '))
# if upper>100:
#     upper=100
# if lower>upper:
#     print("Invalid")
# else:
#     print("fahr celsius")
#     for fahr in range(lower,upper+1,2):
#         celsius=5*(fahr-32.0)/9
#         print("%d%6.1f"%(fahr,celsius))
# a,n=input().split(' ')
# sum=0
# for i in range(1,int(n)+1):
#     sum+=int(a*i)
#     print(a*i)
# print(sum)
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
    

    

    