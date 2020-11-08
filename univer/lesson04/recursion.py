# n!  = n* (n-1)!    5*4*3*2*1
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


def fact_cycle(n):
    x = 1
    for i in range(2, n + 1, 1):
        x *= i
    return x


if __name__ == '__main__':
    print(fact(5))
    print(fact_cycle(5))
