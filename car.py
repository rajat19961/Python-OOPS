from vehicle import Vehicle
class Car(Vehicle):
    numCars = 0

    def __init__(self):
        pass

    def __init__(self,speed,model,color):
        self.speed = speed
        self.model = model
        self.color = color

    def getSpeed(self):
        return self.speed
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def setSpeed(self,speed):
        self.speed = speed

    def setModel(self,model):
        self.model = model

    def setColor(self,color):
        self.color = color

    #overriding abstract method
    def print(self):
        printMessage = "Car Model = "+self.getModel()+"\n"
        printMessage += "Speed = "+str(self.getSpeed())+" Mph"+"\n"
        printMessage += "Color = "+self.getColor()+"\n"
        print(printMessage)

    def decelerate(self):
        self.speed = self.speed - 10

    def accelerate(self):
        self.speed = self.speed + 10

    @staticmethod
    def getNumCars():
        return Car.numCars