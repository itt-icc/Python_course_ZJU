import math
n=int(input())
for i in range(0,n+1):
    print(f"pow({n},{i}) = {int(math.pow(n,i))}")