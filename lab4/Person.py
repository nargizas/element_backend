class Person:
    full_name: str
    age: int

    def __init__(self, full_name, age) -> None:
        self.full_name = full_name
        self.age = age

    def __str__(self) -> str:
        return f"{self.full_name} ({self.age} years old)"
