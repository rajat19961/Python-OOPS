from car import Car
class EV(Car):
    def __init__(self):
        pass
    
    def __init__(self,speed,model,color,range,gen):
        super().__init__(speed,model,color)
        self.range = range
        self.gen = gen

    def getRange(self):
        return self.range

    def getGen(self):
        return self.gen

    def setRange(self,range):
        self.range = range

    def setGen(self,gen):
        self.gen = gen

    def print(self):
        printMessage = "Car Model = "+self.getModel()+"\n"
        printMessage += "Speed = "+str(self.getSpeed())+" Mph"+"\n"
        printMessage += "Color = "+self.getColor()+"\n"
        printMessage += "Range = "+str(self.getRange())+" Miles"+"\n"
        printMessage += "Gen = "+str(self.getGen())+"\n"
        print(printMessage)
