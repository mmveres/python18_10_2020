# 7. Характеристикой строки целочисленной матрицы
# назовем сумму ее положительных четных элементов.
#    Переставляя строки заданной матрицы,
# расположить их в соответствии с ростом характеристик.
from ua.python18_10_2020.univer.lesson03.tasks_matrix import print_matrix


def sort_matrix(matrix):
    sum_row_list = []
    for i in range(len(matrix)):
        sum_row = 0
        for j in range(len(matrix[i])):
            sum_row += matrix[i][j]
        sum_row_list.append(sum_row)

    print(sum_row_list)
    for i in range(len(sum_row_list)):
        for j in range(len(sum_row_list) - 1 - i):
            if sum_row_list[j] < sum_row_list[j + 1]:
                temp = sum_row_list[j]
                t_row = matrix[j]

                sum_row_list[j] = sum_row_list[j + 1]
                matrix[j] = matrix[j+1]

                sum_row_list[j + 1] = temp
                matrix[j+1]=t_row
    print(sum_row_list)
    print_matrix(matrix)


def bubblesort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            count += 1
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(count)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 5],
              [2, 4, 7, 8],
              [1, 2, 1, 2]
              ]
    sort_matrix(matrix)