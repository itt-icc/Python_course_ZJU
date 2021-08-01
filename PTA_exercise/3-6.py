S=list(map(int,input().split(' ')))
number=[]
for i in S:
    number.append(S.count(i))
print(number)
print("{} {}".format(S[number.index(max(number))],max(number)))