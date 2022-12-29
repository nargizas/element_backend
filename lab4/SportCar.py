from Car import Car


class SportCar(Car):
    speed: int

    def __init__(self, marka, car_class, weight, driver, engine, speed) -> None:
        super().__init__(marka, car_class, weight, driver, engine)
        self.speed = speed

    def __str__(self) -> str:
        return super().__str__() + f"Its max speed is {self.speed}"
