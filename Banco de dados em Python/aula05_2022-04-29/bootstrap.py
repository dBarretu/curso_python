import mariadb


if __name__ == '__main__' :

    connection= mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor= connection.cursor()

    #agora vou criar um banco de dados com o mariadb

    sql= "CREATE DATABASE IF NOT EXISTS 20220429_aula05 "
    cursor.execute(sql)
    cursor.execute("use 20220429_aula05")

    #AGORA CRIANDO UMA TABELA DE USUÁRIO...
    sql_users = " CREATE TABLE IF NOT EXISTS sql_users" \
         "(id int not null auto_increment," \
         "name varchar(200) not null," \
         "email varchar (200) not null, " \
         "primary key (id));"
    cursor.execute(sql_users)


    sql_accounts = """
        CREATE TABLE IF NOT EXISTS sql_account
         (id int not null auto_increment,
        user_id int not null,
         name varchar (200) not null,
         balance float not null default(0),
         primary key (id),
        FOREIGN KEY (user_id) references sql_users(id));"""
    cursor.execute(sql_accounts)

    sql_transactions = """CREATE TABLE IF NOT EXISTS sql_transactions
                      (id int not null auto_increment,
                      value float not null,
                      timestamp datetime default now(),
                      credit_account_id int not null, 
                      debit_account_id int not null,
                      primary key (id), 
                      foreign key (credit_account_id) references sql_account(id),
                      foreign key (debit_account_id) references sql_account(id))"""
    cursor.execute(sql_transactions)
