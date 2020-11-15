import json


def get_user():
    dictData = {
        "ID": 210450,
        "login": "admin",
        "name": "John Smith",
        "password": "root",
        "phone": 5550505,
        "email": "smith@mail.com",
        "online": True
    }
    return dictData

def get_3_users():
    user1 = {
        "ID": 1,
        "login": "admin",
        "name": "John Smith",
        "password": "root",
        "phone": 5550505,
        "email": "smith@mail.com",
        "online": True
    }
    user2 = {
        "ID": 2,
        "login": "admin",
        "name": "John Smith",
        "password": "root",
        "phone": 5550505,
        "email": "smith@mail.com",
        "online": True
    }
    user3 = {
        "ID": 3,
        "login": "admin",
        "name": "John Smith",
        "password": "root",
        "phone": 5550505,
        "email": "smith@mail.com",
        "online": True
    }
    users = {
        "user1": user1,
        "user2": user2,
        "user3": user3,
    }
    return users


def write_to_json_file():
    dictData = get_3_users()
    print(dictData)
    dictData["user1"]["skype"] = "@john_smt"
    print(dictData)
    jsonData = json.dumps(dictData)
    print(jsonData)
    with open("users.json_example", "w") as json_file:
        json_file.write(jsonData)


def read_from_json():
    with open("users.json_example", "r") as json_file:
        users_str = json_file.read()
    users_dict = json.loads(users_str)
    print(users_dict["user1"]["skype"])
    for user_key in users_dict:
        print(user_key, " = ", users_dict[user_key])


if __name__ == '__main__':
   pass