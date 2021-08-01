n=int(input())
count=0
for x in range(int(n/5),0,-1):
    for y in range(int((n-5*x)/2),0,-1):
        for z in range(n-5*x-2*y,0,-1):
            if x*5+y*2+z==n:
                print(f"fen5:{x}, fen2:{y}, fen1:{z}, total:{x+y+z}")
                count+=1
print(f"count = {count}")