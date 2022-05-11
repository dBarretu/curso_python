import mariadb
import csv

if __name__ == '__main__':

    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()

    cursor.execute("USE 20220429_aula05")

    cursor.execute("SELECT * FROM sql_users")
    response = cursor.fetchall()

    if len(response) == 0:
        with open(file="users.csv", mode="r") as _file:
            csv_reader = csv.DictReader(_file, delimiter=';')

            for user in csv_reader:
                sql = f"""
                    INSERT INTO sql_users(name, email) VALUES
                        ('{user['name']}', '{user['email']}')
                """
                cursor.execute(sql)

            connection.commit()