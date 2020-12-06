from ua.python18_10_2020.univer.lesson07.inheritance.helper import Helper
from ua.python18_10_2020.univer.lesson07.inheritance.humans import *
def human_get_name(human):
    print(human.name)

if __name__ == '__main__':
    st1 = Student("Tom", 1)
    doc1 = Doctor("AyBolit", 777)
    fight1 = Fighter("BrusLee",100,75)

    humans = [st1,doc1,fight1]
    for human in humans:
        human_get_name(human)

    for human in humans:
        human.eat()
    Helper.save_human_to_file(humans)