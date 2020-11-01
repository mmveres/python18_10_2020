from ua.python18_10_2020.univer.lesson03.tasks_list import *


def main_menu():
    mylist, list_even, list_odd = [], [], []
    while True:
        print("""1.создайте массив, содержащий 10 первых нечетных чисел. 
        Выведете элементы массива на консоль в одну строку, разделяя запятой""")
        print("2.ввести 10 целых значений с консоли и разместить в 2 масива четные и нечетные")
        print("3.подсчитать сколько четные и нечетные")
        print("4.сумма елементов в каждом масиве и среднее арифметическое")
        print("5.поменять четные позиции в первом масиве на значения нечетных позиций из 2 массива")
        print("""6.Дан массив размерности N,  найти наименьший элемент массива
        и вывести на консоль (если наименьших элементов несколько — вывести их индексы).""")
        print("""7.Поменять наибольший и наименьший элементы массива местами.""")
        print("0.Exit")
        answer = int(input("Enter choice"))
        if answer == 1:
            task1_v1()
        elif answer == 2:
            mylist = get_list_from_console()
            print(mylist)
            if len(mylist) > 0:
                list_even, list_odd = get_list_even_odd(mylist)
                print(list_even)
                print(list_odd)
            else:
                print("Empty list, choice first 1.")
        elif answer == 3:
            print_count_even_odd_list(list_even, list_odd)
        elif answer == 4:
            print("sum odd list= ", get_sum_list(list_odd))
            print("average odd list= ", get_average_list(list_odd))
            print("sum even list= ", get_sum_list(list_even))
            print("average even list= ", get_average_list(list_even))
        elif answer == 5:
            print(list_even)
            print(list_odd)
            swap_even_odd_index(list_even, list_odd)
            print(list_even)
            print(list_odd)
        elif answer == 6:
            print("value and index min element in list_even")
            print_value_and_index_min_element_in_list(list_even)
            print("value and index min element in list_odd")
            print_value_and_index_min_element_in_list(list_odd)
        elif answer == 7:
            print(" min max swap even")
            swap_min_max_in_list(list_even)
            print(list_even)
            print(" min max swap odd")
            swap_min_max_in_list(list_odd)
            print(list_odd)
        elif answer == 0:
            break;


if __name__ == '__main__':
    main_menu()
