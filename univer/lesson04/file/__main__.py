from ua.python18_10_2020.univer.lesson04.__main__ import bubblesort


def save_to_file_from_console():
    arr_int = []
    n = int(input("Enter count of value"))
    for i in range(n):
        arr_int.append(int(input("enter int ")))
    with open("data.txt", "w") as file_data:
      #  file_data.writelines(arr_int)
        for x in arr_int:
            file_data.write(str(x))
            file_data.write("\n")


def get_list_from_file(filename):
    arr_int = []
    with open(filename, "r") as file_data:
        for line in file_data:
            arr_int.append(int(line))
    return arr_int

def get_matrix_from_file_with_space(filename):
    matrix_int = []
    with open(filename, "r") as file_data:
        for line in file_data:
            words = line.split(" ")
            row = []
            for word in words:
                row.append(int(word))
            matrix_int.append(row)
    return matrix_int

def get_matrix_from_file_CSV(filename):
    matrix_int = []
    with open(filename, "r") as file_data:
        for line in file_data:
            words = line.split(";")
            row = []
            for word in words:
                row.append(int(word))
            matrix_int.append(row)
    return matrix_int

def print_sum_row_matrix(matrix):
    for i in range(len(matrix)):
        sum_row = 0
        for j in range(len(matrix[i])):
            sum_row += matrix[i][j]
        print(sum_row)


if __name__ == '__main__':

    matrix = get_matrix_from_file_CSV("info.csv")
   # matrix = [[1,2,3,4],[4,5,6,6]]
    print(matrix)
    print_sum_row_matrix(matrix)

