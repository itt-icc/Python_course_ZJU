searchList=list(map(int,input().split()))
price=[0,3.00,2.50,4.10,10.20]
print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit")
count=0
for i in searchList:
    if i==0 or count==5:
        break
    if str(i) in '1234':
        print(f"price = {price[i]:.2f}")
    else:
        print(f"price = {0:.2f}")
    count+=1