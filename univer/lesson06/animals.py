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
        if isinstance(mouse, Mouse):
            print(self.name, "eating name =", mouse.name)
            self.weight+=mouse.weight
            self.mouses.append(mouse)
            mouse.weight = 0
            mouse.killer = self
            mouse.time_kill = datetime.now()
            if self.weight>13:
                self.weight = 0
        else:
            cat_error_eat = "Cat error eat, error its not mouse"
            print(cat_error_eat)
            with open("cat.log", "w") as log_data:
                log_data.write(f"{cat_error_eat},{datetime.now()}")

    def show(self):
        if self.weight>0:
            print("Cat :", self.name, self.year, self.weight)
        else:
            print(self.name, "Cat fat dead...." )

        print("Mouse eaten:")
        for mouse in self.mouses:
            print(mouse.name)


class Mouse:
    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight
        self.killer = None
        self.time_kill =None

    def eat(self, food):
        if 0 < food < self.weight:
            print(self.name, "eating food =", food)
            self.weight+=food
        else:
            print(f"Error food must be in ({0} : {self.weight})")

    def show(self):
        if self.weight>0:
            print("Mouse :", self.name, self.weight)
        else:
            if isinstance(self.killer, Cat):
                print(self.name, "...RIP... kill by ", self.killer.name,self.time_kill )
            else:
                print(self.name, "...RIP... kill by ", self.killer)