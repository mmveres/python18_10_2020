import json

# 1. Прочитать из файла info3.json данные в dict
def dict_from_json(file_name="info.json"):
    with open(file_name, "r") as info_file:
        info_str = info_file.read()
    info_dict = json.loads(info_str)
    return info_dict

# 2. Отобразить количество хобби сотрудника и вывести их на екран
def print_count_of_hobbies(info_dict):
    list_hobbies = info_dict["hobbies"]
    print(list_hobbies)
    print(len(list_hobbies))

# 3. Сколько детей у сотрудника
def get_count_of_childrens(info_dict):
    list_childrens = info_dict["children"]
    return len(list_childrens)

# 4. Вывести имя старшего ребенка
def get_older_of_childrens(info_dict):
    list_childrens = info_dict["children"]
    old_child = list_childrens[0]
    for child in list_childrens:
        if child["age"]> old_child["age"]:
            old_child = child
    return old_child

# 5. Добавить в dict сотрудника ключ "email": jane@company.com , "phone": 123456
# и сохранить в новый файл info2.json
def write_dict_to_json(info_dict, file_name = "info2.json"):
    with open(file_name, "w", encoding="cp1251") as info_file:
        info_file.write(json.dumps(info_dict))

def update_and_write_dict_to_json(info_dict):
    info_dict["email"] = "jane@company.com"
    info_dict["phone"] = "123456"
    print(info_dict)
    write_dict_to_json(info_dict)