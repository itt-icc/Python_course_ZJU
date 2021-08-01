n=int(input())
item=10**(n-1)
while item<10**(n):
    num=item
    sum=0
    for i in range(0,n):
        digit=num%10
        num=num//10
        sum+=digit**n
    if sum==item:
        print(item)
    item+=1
# item=372
# num=item
# sum=0
# for i in range(0,3):
#     digit=num%10
#     num=num//10
#     sum+=digit**3
# if sum==item:
#     print(item)