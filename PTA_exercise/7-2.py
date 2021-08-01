n=int(input())
l=[]
for i in range(n):
    student=input().split()
    l.append(student)
l2=l[::-1]
for i in range(int(n/2)):
    couple=[]
    couple.append(l[i][1])
    for j in l2:
        if j[0]!=l[i][0]:
            couple.append(j[1])
            l2.remove(j)
            break
    print(*couple,sep=" ")
    