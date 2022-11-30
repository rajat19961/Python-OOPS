from car import Car
from ev import EV

if __name__ == "__main__":
    firstCar = Car(100,"Ford Mustang","Yellow")
    firstCar.print()
    Car.numCars = Car.getNumCars() + 1
    print("Total number of Cars now = "+str(Car.getNumCars())+"\n")
    #Illustrating various methods
    firstCar.setSpeed(200)
    firstCar.accelerate()
    firstCar.accelerate()
    firstCar.decelerate()
    firstCar.setModel("Ford Mustang GT")
    firstCar.setColor("Red")
    print("New Speed of 1st car = "+str(firstCar.getSpeed()) +" Mph")
    print("New Model of 1st car = "+firstCar.getModel())
    print("New Color of 1st car = "+firstCar.getColor())
    
    #Creating EV car
    evCar = EV(130,"Tesla Model 3","White",220,3)
    evCar.print()
    Car.numCars = Car.getNumCars() + 1
    print("Total number of Cars now = "+str(Car.getNumCars())+"\n")

    #Illustrating set methods and get methods
    evCar.setSpeed(155)
    evCar.accelerate()
    evCar.accelerate()
    evCar.decelerate()
    evCar.setModel("Tesla Model S")
    evCar.setColor("Black")
    evCar.setRange(402)
    evCar.setGen(2)
    print("New Speed of EV car = "+str(evCar.getSpeed()) +" Mph")
    print("New Model of EV car = "+evCar.getModel())
    print("New Color of EV car = "+evCar.getColor())
    print("New Range of EV car = "+str(evCar.getRange()) + " Miles")
    print("New Gen of EV Car = "+str(evCar.getGen()))