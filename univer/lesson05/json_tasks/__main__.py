import json

from ua.python18_10_2020.univer.lesson05.json_tasks.json_task import *

if __name__ == '__main__':
    info_dict = dict_from_json("info3.json")
    print(info_dict)
    list_childrens = []
    for info_key in info_dict:
       # print_count_of_hobbies(info_dict[info_key])
       # print(get_older_of_childrens(info_dict[info_key]))
       for child in info_dict[info_key]["children"]:
            list_childrens.append(child["firstName"])
    print("count of child =",len(list_childrens))
    print("unique name =",set(list_childrens))
