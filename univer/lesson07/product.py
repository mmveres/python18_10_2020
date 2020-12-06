from ua.python18_10_2020.univer.lesson07.currency import Currency

class ProductException(Exception):
    def __init__(self, message):
        super.__init__(message)


class Product:
    def __init__(self, name, weight, price):
        self.__name = name
        self.weight = weight
        self.price = price

    @property
    def price(self):
        return self.__price*Currency.usd*1.20

    @price.setter
    def price(self, value):
        if(value>0):
            self.__price = value/Currency.usd
        else:
            print("Error not valid value of price")

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ProductException("Error not valid value of weight")

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.price}"
