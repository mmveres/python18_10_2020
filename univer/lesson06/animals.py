from datetime import datetime


class Cat:
    def __init__(self, name, year, weight):
        self.__name = name
        self.__year = year
        self.__weight = weight
        self.__mouses = []

    def get_name(self):
        return self.__name

    def set_year(self, year):
        if year in range(1,100):
            self.__year = year
        else:
            print("Error year value")

    def get_year(self):
        return self.__year

    def set_weight(self, weight):
        if 0<weight<10:
            self.__weight = weight
        else:
            print("error weight value")

    def get_weight(self):
        return self.__weight

    def get_mouses(self):
        return self.__mouses

    def eat(self, food):
        print(self.__name, "eating food =", food)
        self.__weight+=food

    def eat_mouse(self, mouse):
        if isinstance(mouse, Mouse):
            print(self.__name, "eating name =", mouse.get_name())
            self.__weight+=mouse.get_weight()
            self.__mouses.append(mouse)
            mouse.set_weight(0)
            mouse.set_killer(self)
            if self.__weight>13:
                self.__weight = 0
        else:
            cat_error_eat = "Cat error eat, error its not mouse"
            print(cat_error_eat)
            with open("cat.log", "w") as log_data:
                log_data.write(f"{cat_error_eat},{datetime.now()}")

    def show(self):
        if self.__weight>0:
            print("Cat :", self.__name, self.__year, self.__weight)
        else:
            print(self.__name, "Cat fat dead...." )

        print("Mouse eaten:")
        for mouse in self.__mouses:
            print(mouse.get_name())


class Mouse:
    def __init__(self, name, weight=1):
        self.__name = name
        self.__weight = weight
        self.__killer = None
        self.__time_kill =None

    def get_name(self):
        return self.__name

    def set_weight(self, weight):
        if 0<=weight<5:
            self.__weight=weight
        else:
            print("error weight value")

    def get_weight(self):
        return self.__weight

    def set_killer(self, killer):
        if isinstance(killer, Cat):
            self.__killer = killer
            self.__time_kill = datetime.now()
        else:
            print("Error killer value")

    def eat(self, food):
        if 0 < food < self.__weight:
            print(self.__name, "eating food =", food)
            self.__weight+=food
        else:
            print(f"Error food must be in ({0} : {self.__weight})")

    def show(self):
        if self.__weight>0:
            print("Mouse :", self.__name, self.__weight)
        else:
            print(self.__name, "...RIP... kill by ", self.__killer.get_name(), self.__time_kill)
