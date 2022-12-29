from Car import Car


class Lorry(Car):
    carrying: int

    def __init__(self, marka, car_class, weight, driver, engine, carrying) -> None:
        super().__init__(marka, car_class, weight, driver, engine)
        self.carrying = carrying

    def __str__(self) -> str:
        return super().__str__() + f"It carries {self.carrying}"
