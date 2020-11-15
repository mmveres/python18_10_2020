import csv
import codecs
from ua.python18_10_2020.univer.lesson05.json_tasks.json_task import write_dict_to_json


def users_csv_dict_example():
    FILENAME = "users.csv"
    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]
    with open(FILENAME, "w", newline="") as file:
        columns = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        # запись нескольких строк
        writer.writerows(users)

        user = {"name": "Sam", "age": 41}
        # запись одной строки
        writer.writerow(user)
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], "-", row["age"])


def csv_to_dict_kmda(file_name):
    with open(file_name, "r", newline="", encoding="cp1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        dict_sum_kmda = dict()
      #  print(reader.fieldnames)
      #  print(reader.fieldnames[0], "-", reader.fieldnames[11])
        for row in reader:
            dict_sum_kmda[row["Працівник"]]=row["Сума"]
    return dict_sum_kmda



if __name__ == '__main__':
    file_name = "zp-lupen-2019.csv"
    kmda_sum = csv_to_dict_kmda(file_name)
    write_dict_to_json(kmda_sum,"kmda_sum.json")

    print(kmda_sum)
    print(kmda_sum.keys())
    print(kmda_sum.values())