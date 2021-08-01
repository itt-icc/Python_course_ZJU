class Stock:
    def __init__(self,symbol,name,preClosingPrice,curPrice):
        self.__symbol=str(symbol)
        self.__name=str(name)
        self.__preClosingPrice=float(preClosingPrice)
        self.__curPrice=float(curPrice)
    def getSymbol(self):
        return self.__symbol
    def getName(self):
        return self.__name
    def setPre(self,pre):
        self.__preClosingPrice=pre
    def getPre(self):
        return self.__preClosingPrice
    def getCur(self):
        return self.__curPrice
    def getChangePercent(self):
        return (self.__curPrice-self.__preClosingPrice)/self.__preClosingPrice*100
        
s=Stock("10001","平头哥芯片",62.8,70.32)
print(s.getName())
print(s.getPre())
print(s.getCur())
print(f"当前涨幅 : {s.getChangePercent():.2f}%")