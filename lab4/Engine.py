class Engine:
    power: int
    company: str

    def __init__(self, power, company) -> None:
        self.power = power
        self.company = company

    def __str__(self) -> str:
        return f"{self.power} {self.company}"
