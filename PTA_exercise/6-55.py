
def funcos(eps,x):
    sum=0
    n=0
    while True:
        numerator=x**n#分子
        denominator=1
        for i in range(1,n+1):
            denominator=denominator*i
        item=((-1.0)**(n/2))*numerator/denominator
        n+=2
        if abs(item)<eps:
            break
        sum+=item
    return sum

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))