from Person import Person
class Teacher(Person):
    def __init__(self, name, age, year, salary):
        super().__init__(name, age,salary)
        self.year= year
    def say_hi(self):
        print(super().say_hi())
        return f"Helloo {self.name} as teacher"
        
    def bounce(self):
       b = super().salary * 2
       return b 