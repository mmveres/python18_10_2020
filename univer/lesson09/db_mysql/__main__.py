import mysql.connector
if __name__ == '__main__':
    conn = mysql.connector.connect(
        host="127.0.0.1:3306",
        user="root",
        password="root",
        database="mymap"
    )
    cursor = conn.cursor()
    cursor.execute("select * from cities")
    result_list = cursor.fetchall()
    print(result_list)
    conn.close()