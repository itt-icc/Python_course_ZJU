
def fn(a,n):
    SUM=0
    for i in range(1,n+1):
        SUM+=int(str(a)*i)
    return SUM
		 
a,b=input().split()
s=fn(int(a),int(b))
print(s)