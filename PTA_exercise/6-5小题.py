# import math
# def factors(x):
#     y=int(math.sqrt(x))
#     for i in range(2,y+1):
#         if (x%i ==0):
#             factors(x//i)
#             break
#         else:
#             print(x,end=' ')
#         return
# factors(38)
# def ins_sort_rec(seq, i):
#     if i == 0: return
#     ins_sort_rec(seq, i - 1)
#     j = i
#     while j > 0 and seq[j - 1] > seq[j]: 
#         seq[j - 1], seq[j] = seq[j], seq[j - 1] 
#         j -= 1
# 
# seq = [3,-6,79,45,8,12,6,8]
# ins_sort_rec(seq, len(seq)-1)
# print(seq)
# print(seq[5])
# def basic_lis(seq):
#     l=[1]*len(seq)
#     for cur ,val in enumerate(seq):           #enumerate返回元素的"索引和值"
#         for pre in range(cur):
#             if seq[pre]<val:
#                 l[cur]=max(l[cur],1+l[pre])
#     print(l)
#     return max(l)
# 
# L=[49, 64, 17, 100, 86, 66, 78, 68, 87, 96, 19, 99, 35]
# print(basic_lis(L))
# def bubble(List):
#     for j in range(len(List)-1,0,-1):
#         for i in range(0,j):
#             if List[i]>List[i+1]:
#                 List[i],List[i+1]=List[i+1],List[i]
#     return List
# 
# testlist = [49, 38, 65, 97, 76, 13, 27, 49]
# print( bubble(testlist))
# def selSort(nums):
#     n = len(nums)
#     for bottom in range(n-1):
#         mi = bottom
#         for i in range(mi+1, n):
#             if nums[i] < nums[mi]:
#                  mi = i
#         nums[bottom], nums[mi] = nums[mi], nums[bottom] 
#     return nums
# 				
# numbers = [49, 38, 65, 97, 76, 13, 27, 49]
# print(selSort(numbers))
def nprintf(message,n):
    for i in range(n):
        print(message,end=" ")


nprintf("a",3,)
nprintf(n=5,message="good")
