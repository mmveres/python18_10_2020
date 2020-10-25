def print_odd(start,end):
    i = start
    while i<end:
        if i%2!=0:
            print(i,end=", ")
        i+=1
    print()
#2. Даны целые числа K и N (N > 0). Вывести N раз число K.
def t02_print_n_k(n,k):
    print("***")
    for i in range(n):
        print(k)
    print("***")

def t02_input_and_print_n_k():
    k = int(input("Enter k"))
    n = int(input("Enter n"))
    t02_print_n_k(n,k)

# 3. Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые  числа,
# расположенные  между  A  и  B (включая  сами  числа  A  и  B),
# а также количество N этих чисел.

def t03_print_asc_a_to_b(a,b):
    if a < b:
        x = a
        count = 0
        while x <= b:
            print(x)
            x+=1
            count+=1
        print("count = ",count)
    else:
        print("Error A>B")

#4. Вывести 10 первых чисел последовательности 0, -5,-10,-15..
def print_10_value(start = 0, step = 5):
    x = start
    for i in range(10):
        print(x)
        x-=step
#5. Дано число n при помощи цикла for посчитать n!( n!=n*(n-1)!)
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact*=i
    return fact
