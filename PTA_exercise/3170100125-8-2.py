class QE:
    def __init__(self,a,b,c):
        self.__a=float(a)
        self.__b=float(b)
        self.__c=float(c)
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__b**2-4*self.__a*self.__c
    def getRoot1(self):
        if self.getD()>=0:
            return (-self.__b-self.getD())/self.__a*0.5
        else:
            return 0
    def getRoot2(self):
        if self.getD()>=0:
            return (-self.__b+self.getD())/self.__a*0.5
        else:
            return 0
a,b,c=map(float,input("请输入a b c:\n").split())
q=QE(a,b,c)
if q.getD()<0:
    print("\n\n该方程式无根")
else:
    print(f"\n\n第1个根为{q.getRoot1():.4f}\n第2个根为{q.getRoot2():.4f}")
    