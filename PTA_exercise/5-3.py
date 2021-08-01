a=int(input())
operation=input()
b=int(input())
if b==0 and operation=='/':
    print("divided by zero")
else:
    res={'+':a+b,'-':a-b,'*':a*b,'/':a/b}
    print(f"{res[operation]:.2f}")
