def get_list_kmda_from_file(filename):
    list_kmda = []
    with open(filename, "r") as file_kmda:
        for line in file_kmda:
            words = line.split(";")
            list_kmda.append(words)
    return list_kmda


def print_name_with_oklad():
    for row in list_kmda:
        print(row[0], row[2])


def get_max_oklad(list_kmda):
    max_oklad = float(list_kmda[1][2].replace(',', '.'))
    for i in range(1, len(list_kmda)):
        if float(list_kmda[i][2].replace(',', '.')) > max_oklad:
            max_oklad = float(list_kmda[i][2].replace(',', '.'))
    return max_oklad

def get_average_oklad(list_kmda):
    sum=0.0
    for i in range(1, len(list_kmda)):
        sum += float(list_kmda[i][2].replace(',', '.'))
    return sum/(len(list_kmda)-1)

def get_list_name_with_max_oklad(list_kmda, max_oklad):
    names_list_with_max_oklad = []
    for i in range(1, len(list_kmda)):
        if float(list_kmda[i][2].replace(',', '.')) >= max_oklad:
            names_list_with_max_oklad.append(list_kmda[i][0])
    return names_list_with_max_oklad

if __name__ == '__main__':
    list_kmda = get_list_kmda_from_file("zp-lupen-2019.csv")
    print(list_kmda)
    print_name_with_oklad()
    max_oklad = get_max_oklad(list_kmda)
    print(max_oklad)
    print(get_list_name_with_max_oklad(list_kmda,max_oklad))
    average_oklad = get_average_oklad(list_kmda)
    print(average_oklad)
    print(get_list_name_with_max_oklad(list_kmda, average_oklad))

