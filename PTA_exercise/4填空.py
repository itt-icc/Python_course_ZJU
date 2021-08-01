# for i in range(1,5):
#     j=0
#     while j<i:
#        print(j,end=" ")
#        j+=1
#     print()
# i=5
# while i>=1:
#     num=1
#     for j in range(1,i+1):
#         print(num,end="xxx")
#         num*=2
#     print()
#     i-=1
# i=1
# while i<=5:
#     num=1
#     for j in range(1,i+1):
#         print(num,end="G")
#         num+=2
#     print()
#     i+=1
# a = [1, 2, 3, 4, [5, 6], [7, 8, 9]]
# s = 0
# for row in a:
#        if type(row)==list:
#             for elem in row:
#                s += elem
#        else:
#             s+=row
# print(s)
# l3=[i+j for i in range(1,6) for j in range(1,6)]
# print(sum(l3))
# l3=[[(i,j) for i in range(1,6)] for j in range(1,6)]
# print(l3)
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)
