import math
from ua.python18_10_2020.univer.lesson02.menu import main_menu
from ua.python18_10_2020.univer.lesson02.tasks import *
def main():
    while True:
        answer = main_menu()
        if answer == 1:
            start = int(input("enter start"))
            end = int(input("enter end"))
            print_odd(start, end)
        elif answer == 2:
            t02_input_and_print_n_k()
        elif answer == 3:
            a = int(input("enter a"))
            b = int(input("enter b"))
            t03_print_asc_a_to_b(a,b)
        elif answer == 4:
            start = int(input("enter start"))
            step = int(input("enter step"))
            print_10_value(start, step)
        elif answer == 5:
            value = int(input("enter n"))
            print("my factorial = ", factorial(n=value))
            print("math.factorial = ", math.factorial(value))
        elif answer == 0:
            break
        else:
            print("Error choice")

main()