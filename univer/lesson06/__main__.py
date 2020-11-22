from ua.python18_10_2020.univer.lesson06.animals import Cat, Mouse

if __name__ == '__main__':
    cat1 = Cat("Tom", 2, 7)
    cat1.show()
    cat1.eat(1.5)
    cat1.show()

    cat2 = Cat("Tomik", 5, 9)
    cat2.eat(0.5)
    cat2.show()

    cat3 = Cat("Tomidze", 10, 11)
    cat3.show()

    m1 = Mouse(name="Jerry", weight=2)
    m1.eat(1)
    m1.show()

    cat1.eat_mouse(cat2)
    cat1.show()
    m1.show()
    m2 = Mouse(name="JerrykoFF", weight=1.5)
    cat1.eat_mouse(m2)
    cat1.show()
    m2.show()

    m3 = Mouse(name="JerryLi", weight=2.5)
    cat1.eat_mouse(m3)
    cat1.show()
    m3.show()