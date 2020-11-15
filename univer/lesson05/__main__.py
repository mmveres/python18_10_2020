def show_params(user_params):
    print("name :", user_params[0])
    print("age :", user_params[1])
    print("id :", user_params[2])
    print("city :", user_params[3])


if __name__ == '__main__':
    #  user = ["Tom", 23, 12345, "Kyiv"]
    with open("user.dat", "r") as user_data:
        user_str = user_data.readline()
    user_params = user_str.split(",")
    user_params = tuple(user_params)
    print(user_params)
    show_params(user_params)
    user_params[1] = -817817
    show_params(user_params)
