from Person import Person


class Driver(Person):
    experience: int

    def __init__(self, full_name, age, experience) -> None:
        super().__init__(full_name, age)
        self.experience = experience

    def __str__(self) -> str:
        return f"{self.full_name} ({self.experience} years xp)"
