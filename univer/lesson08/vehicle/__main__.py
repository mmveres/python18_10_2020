from ua.python18_10_2020.univer.lesson08.vehicle.vehicles import *

if __name__ == '__main__':
    car1 = Car(10,5,100)
    ship1 = Ship(20, 7, 70,50)
    amph1 = Amphibia(15,6,80)

    vehicles = [car1, ship1, amph1, Amphibia(16,6,85), Ship(25, 7, 70,55),BatMobile()]

    swimable_list = list()
    for veh in vehicles:
        if isinstance(veh, SwimAble):
           # veh.print()
           # veh.swim()
            swimable_list.append(veh)

    for swim in swimable_list:
        swim.print()