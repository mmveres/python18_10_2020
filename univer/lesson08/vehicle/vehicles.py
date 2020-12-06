import abc
class SwimAble(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def swim(self):
        pass

class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self,price,year,speed):
        self.price = price
        self.year = year
        self.speed = speed
    @abc.abstractmethod
    def print(self):
        pass

class Car(Vehicle):
    def __init__(self,price,year,speed):
        super().__init__(price,year,speed)

    def print(self):
        print("Car", self.price, self.year, self.speed)

class Ship(Vehicle, SwimAble):
    def __init__(self,price,year,speed, count_pass):
        super().__init__(price,year,speed)
        self.count_pass = count_pass

    def swim(self):
        return self.speed

    def print(self):
        print("Ship", self.price, self.year, self.speed, self.count_pass)

class Amphibia(Car, SwimAble):
    def __init__(self,price,year,speed):
        super().__init__(price,year,speed)
    def move(self):
        return self.speed
    def swim(self):
        return self.speed/2

    def print(self):
        print("Amphibia", self.price, self.year, self.speed)

class BatMobile:
    #ToDo implement class
    pass
