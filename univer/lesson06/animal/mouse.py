

class Mouse:
    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight
        self.killer = None
        self.time_kill = None

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
            print(self.name, "...RIP... kill by ", self.killer.name)
