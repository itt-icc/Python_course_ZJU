n=int(input())
Slist=list(map(int,input().split()))
if n==0:
    print(f"average = {0:.1f}")
else:
    print(f"average = {sum(Slist)/float(n):.1f}")
c=[i for i in Slist if i>= 60 ]
print(f"count = {len(c)}")