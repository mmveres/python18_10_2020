from ua.python18_10_2020.univer.lesson06.animals import Cat, Mouse
from ua.python18_10_2020.univer.lesson06.cats_controller import Cats


def tom_eat_mouse():
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





if __name__ == '__main__':
    cat1 = Cat("Tom", 2, 4)
    cat2 = Cat("Tomik", 4, 7)
    cat3 = Cat("Tomidze", 3, 9)
    cat4 = Cat("Tomik", 4, 8)

    old_cat = cat1
    if(old_cat.get_year()< cat2.get_year()):
        old_cat = cat2
    if (old_cat.get_year() < cat3.get_year()):
        old_cat = cat3

    print("old cat")
    old_cat.show()

    cat_list = [cat1, cat2, cat3]

    fat_cat = Cats.get_fat_cat(cat_list)

    print("Fat cat")
    fat_cat.show()