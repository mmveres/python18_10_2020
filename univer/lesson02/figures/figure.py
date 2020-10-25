def print_rectangle(start =0, end = 9):
    for i in range(end+1):
        for j in range(end+1):
            if i == start or i == end or j == start or j == end:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def print_right_triangle():
    for i in range(10):
        for j in range(10):
            if i == 9 or j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def print_equilateral_triangle():
    pass


def print_rhombus():
    pass