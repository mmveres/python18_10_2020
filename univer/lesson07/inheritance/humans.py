class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating")

    def __str__(self):
        return f"{self.name}"

class Student(Human):
    def __init__(self,name,group):
        super().__init__(name)
        self.group = group

    def study(self):
        print("study")

    def eat(self):
        print("student eat")

    def __str__(self):
        return f"{super().__str__()}, {self.group}"

class Doctor(Human):
    def __init__(self,name,license):
        self.license = license
        super().__init__(name)

    def cure(self):
        print("cure")

    def __str__(self):
        return f"{self.name}, {self.license}"

class Fighter(Human):
    def __init__(self,name,power, defence):
        super().__init__(name)
        self.power = power
        self.defence = defence

    def fight(self):
        print("fight")

    def __str__(self):
        return f"{self.name}, {self.power}, {self.defence }"

