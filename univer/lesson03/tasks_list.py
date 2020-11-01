# 1.создайте массив, содержащий 10 первых нечетных чисел.
# Выведете элементы массива на консоль в одну строку, разделяя запятой
# 2.ввести 10 целых значений с консоли и разместить в
# 2 масива четные и нечетные
# 3.подсчитать сколько четные и нечетные
# 4.сумма елементов в каждом масиве и среднее арифметическое
# 5.поменять четные позиции в первом масиве на значения
# нечетных позиций из 2 массива
# 6.Дан массив размерности N,  найти наименьший элемент массива
# и вывести на консоль (если наименьших элементов несколько —
# вывести их индексы).
# 7.Поменять наибольший и наименьший элементы массива местами.
# Пример: дан массив {4, -5, 0, 6, 8}.
# После замены будет выглядеть {4, 8, 0, 6, -5}.
import random


def task1_v1():
    mylist = list(range(1, 20, 2))
    print(mylist)


def task1_v2():
    mylist = list()  # []
    for i in range(20):
        if i % 2 == 1:
            mylist.append(i)
    print(mylist)


def task1_v3():
    mylist = []
    i = 0
    count_odd = 0
    while count_odd < 10:
        if i % 2 != 0:
            mylist.append(i)
            count_odd += 1
        i += 1
    print(mylist)


def task1_v4():
    mylist = []
    i = random.randint(1, 100)
    count_odd = 0
    while count_odd < 10:
        if i % 2 != 0:
            mylist.append(i)
            count_odd += 1
        i = random.randint(1, 100)
    print(mylist)


def get_list_10_int_random():
    return list(random.sample(list(range(100)), 10))


def get_list_10_int():
    return list(range(10))


def get_list_from_console():
    mylist = []
    for i in range(10):
        value = int(input(f"Enter {i} value: "))
        mylist.append(value)
    return mylist


def get_list_even_odd(mylist) -> (list, list):
    list_odd = []
    list_even = []
    for i in range(10):
        value = mylist[i]
        if value % 2 == 0:
            list_even.append(value)
        else:
            list_odd.append(value)
    return list_even, list_odd


def print_count_even_odd_list(list_even: list, list_odd: list) -> None:
    print(len(list_even))
    print(len(list_odd))


def get_sum_list(list_elem):
    sum = 0
    for elem in list_elem:
        sum += elem
    return sum


def get_average_list(list_elem):
    return get_sum_list(list_elem) / len(list_elem)


def print_value_and_index_min_element_in_list(list_elem):
    min_elem = min(list_elem)
    print("min value",min_elem)
    min_count = list_elem.count(min_elem)
    print("min count", min_count)
    for i in range(len(list_elem)):
        if list_elem[i] == min_elem:
            print("index =", i)


def swap_even_odd_index(list_even, list_odd):
    count = 0
    if len(list_even) < len(list_odd):
        count = len(list_even)
    else:
        count = len(list_odd)
    for i in range(count):
        if i%2 != 0:
            temp = list_even[i]
            list_even[i]=list_odd[i]
            list_odd[i]=temp


def swap_min_max_in_list(list_elem):
    min_elem = min(list_elem)
    max_elem = max(list_elem)
    for i in range(len(list_elem)):
        if list_elem[i] == min_elem:
            list_elem[i] = max_elem
        elif list_elem[i] == max_elem:
            list_elem[i] =min_elem


if __name__ == '__main__':
    mylist = [1,2,43,43,4,1]
    swap_min_max_in_list(mylist)
    print(mylist)