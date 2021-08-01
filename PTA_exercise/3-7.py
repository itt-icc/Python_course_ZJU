n=int(input())
s = list(map(int,input().split()))
max=s[0]
for i in range(len(s)):
    if s[i]>max:
        max=s[i]
        idx=i
print("{} {}".format(idx,max))