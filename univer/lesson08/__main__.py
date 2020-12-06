from ua.python18_10_2020.univer.lesson08.figures import *
def printArea(shape):
    print(shape.area())

if __name__ == '__main__':
    r1 = Rectangle(2,3)
    printArea(r1)

    shape1 = Shape()
    print(shape1.area())