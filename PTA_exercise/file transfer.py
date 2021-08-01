n=int(input())
net=set()
count=0
while True:
    inpu=input().split()
    operation=inpu[0]
    if operation=="S":break
    c1,c2=int(inpu[1]),int(inpu[2])
    if operation=="C":
        if c1 in net and c2 in net:
            print("yes")
            count+=1
        else:
            print("no")
    else:
        net.add(c1)
        net.add(c2)
    print(net)
if len(net)==n:
    print(f"The network is connected.")
else:
    print(f"There are {count} components.")