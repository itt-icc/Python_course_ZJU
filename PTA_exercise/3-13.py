# s=input()
# new=''
# for i in s:
#     if ord(i)<=90 and ord(i)>=65:#大写字母
#         new+=i.lower()
#     elif ord(i)<=122 and ord(i)>=97:#小写字母
#         new+=i.upper()
#     elif i=='#':
#         pass
#     else:
#         new+=i
# print(new)
print(input().swapcase()[:-1])
# for i in (10,9,8,7,6,5,4,3,2,1):print(i)