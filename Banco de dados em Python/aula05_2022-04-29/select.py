import mariadb

if __name__ == '__main__':
    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()
    cursor.execute("USE 20220429_aula05")

    sql_users=  "SELECT * FROM sql_users"
    cursor.execute(sql_users)

    response = cursor.fatchall()

    for user in response:
        print(user)

    for user in response:
        print(user)

    sql_account = "SELECT * FROM sql_account"
    cursor.execute (sql_account)

    response= cursor.fatchone()
    print(response)

    sql_transactions = "SELECT * FROM sql_transactions"
    cursor.execute(sql_transactions)

    response.fatchmany