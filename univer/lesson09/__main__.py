import sqlite3

from ua.python18_10_2020.univer.lesson09.employee import Employee


def print_employee():
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    cursor.execute("select * from Employee")
    result_list = cursor.fetchall()
    for result in result_list:
        print("second name :", result[1], "first name :", result[2], " email:", result[14])
    conn.close()

def get_employees_from_db(dbname = "Chinook_Sqlite.sqlite"):
    empl_list = []
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("select * from Employee")
    result_list = cursor.fetchall()
    for result in result_list:
        empl_list.append(Employee(second_name=result[1],first_name= result[2],email= result[14]))
    conn.close()
    return empl_list

def save_employee_to_csv(employees):
    with open("empl.csv", "w") as file_data:
        for empl in employees:
            file_data.write(empl.__str__())
            file_data.write("\n")

def insert_employee(second_name, first_name, email):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        sql_insert = f"""
        insert into Employee(LastName,      FirstName,     Email) 
        values        ('{second_name}','{first_name}', '{email}')
        """
        cursor.execute(sql_insert)
        conn.commit()


def insert_employee_param1(empl):
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    sql_insert = "insert into Employee(LastName,FirstName,Email) values(?,?,?)"
    cursor.execute(sql_insert,(f'{empl.second_name}',f'{empl.first_name}',f'{empl.email}'))
    conn.commit()
    conn.close()

def insert_employee_param2(second_name, first_name, email):
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    sql_insert = "insert into Employee(LastName,FirstName,Email) values(:s_name,:f_name,:email)"
    cursor.execute(sql_insert,
                   {"s_name": f'{second_name}',
                    "f_name": f'{first_name}',
                     "email": f'{email}'}
                   )
    conn.commit()
    conn.close()

def update_employee_second_name(second_name, second_name_change):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        sql_update = "update Employee set LastName = :s_name_change where LastName = :s_name"
        cursor.execute(sql_update, {
                   "s_name": f'{second_name}',
            "s_name_change": f'{second_name_change}'
        })
        conn.commit()

if __name__ == '__main__':
    print_employee()
  #  empl = Employee("Shevchenko","Taras", "taras@shevchenko.ua")
  #  insert_employee_param1(empl)
  #  update_employee_second_name("Bezos1","Kuk1")
    employees=get_employees_from_db()
    save_employee_to_csv(employees)