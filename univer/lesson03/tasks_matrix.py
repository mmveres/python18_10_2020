# Двумерные массивы
# Дана целочисленная прямоугольная матрица.
# 1. Вывести все положительные елементы;
def print_positive_elem_matrix():
    #TODO реализовать функцію
    pass

# 2. Вывести количество строк, не содержащих
# ни одного нулевого элемента;

# 3. Вывести номера столбцов, содержащих хотя бы
# один нулевой элемент;

# 4. Вывести количество строк и номера строк в
# которых есть отрицательные елементы.

# 5. Вывести максимальное из чисел,
# встречающихся в заданной матрице более одного раза.

# 6. Вывести номер строки, в которой находится
# самая длинная серия одинаковых элементов.

# 7. Характеристикой строки целочисленной матрицы
# назовем сумму ее положительных четных элементов.
#    Переставляя строки заданной матрицы,
# расположить их в соответствии с ростом характеристик.


def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end="\t")
        print()


def print_sum_matrix(matrix):
    all_sum_matrix = 0
    for i in range(len(matrix)):
        # ---before i row
        row_sum_matrix = 0
        # ---
        for j in range(len(matrix[i])):
            # ---for each j cell i row
            row_sum_matrix += matrix[i][j]
            if matrix[i][j] % 2 == 0:
                print(matrix[i][j], end="\t")
            else:
                print("-", end="\t")
            # ---
        # ---after i row
        print()
        print("sum_matrix row=", row_sum_matrix)
        all_sum_matrix += row_sum_matrix
        # ---
    print("sum_matrix =", all_sum_matrix)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [6, 7, 8, 9, 5, 7],
        [3, 3, 3, 3, 4]
    ]
    print(len(matrix))
    print(len(matrix[0]))
    print(len(matrix[1]))
    print(len(matrix[2]))
    print_sum_matrix(matrix)

    print_matrix(matrix)
