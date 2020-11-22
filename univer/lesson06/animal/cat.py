from datetime import datetime


class Cat:
    def __init__(self, name, year, weight):
        self.name = name
        self.year = year
        self.weight = weight
        self.mouses = []

    def eat(self, food):
        print(self.name, "eating food =", food)
        self.weight+=food

    def eat_mouse(self, mouse):
        print(self.name, "eating name =", mouse.name)
        self.weight+=mouse.weight
        self.mouses.append(mouse)
        mouse.weight = 0
        mouse.killer = self
        mouse.time_kill = datetime.now()
        if self.weight>13:
            self.weight = 0


    def show(self):
        if self.weight>0:
            print("Cat :", self.name, self.year, self.weight)
        else:
            print(self.name, "Cat fat dead...." )

        print("Mouse eaten:")
        for mouse in self.mouses:
            print(mouse.name)