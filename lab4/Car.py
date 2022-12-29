from Driver import Driver
from Engine import Engine


class Car:
    marka: str
    car_class: str
    weight: int
    driver: Driver
    engine: Engine

    def __init__(self, marka, car_class, weight, driver, engine) -> None:
        self.marka = marka
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start():
        print("Поехали")

    def stop():
        print("Останавливаемся")

    def turn_right():
        print("Поворот направо")

    def turn_left():
        print("Поворот налево")

    def __str__(self) -> str:
        return f"This car is {self.marka} of {self.car_class} class. Its weight is {self.weight}. The driver is {self.driver}. Its engine is {self.engine}. "
