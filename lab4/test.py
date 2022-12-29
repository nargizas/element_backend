from Car import Car
from Driver import Driver
from Engine import Engine
from Lorry import Lorry
from Person import Person
from SportCar import SportCar

person = Person("Alice Bob", 28)
print(person)

driver = Driver("Mitchell Clark", 32, 5)
print(driver)

engine = Engine(18, "ABC")
print(engine)

car = Car("BMW", "S", 180, driver, engine)
print(car)

sport_car = SportCar("BMW", "S", 180, driver, engine, 300)
print(sport_car)

lorry = Lorry("X", "X", 2000, driver, engine, 250)
print(lorry)
