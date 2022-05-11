#esse script irá criar a estrutura inicial de banco de dados

#importamos o conector do mariadb
import mariadb

"""
Quando trabalhamos com conectores, geralmente utilizamos dois objetos:
    -O OBJETO DE CONEXÃO
    - O OBJETO CURSOR 
    
Pirmeiro criamos a conexão com o banco de dados, e depois utilizamos essa conexão para
criar o cursor, onde a partir dele iremos executar os comandos no banco de dados


Na computação, o termo localhost se refere à localização do sistema que está sendo usado.
"""

if __name__ == '__main__':

    connection  = mariadb.connect(
        host= "localhost",
        user= "root",
        password= ""
    )

    cursor = connection.cursor()

    #criando o banco de dados
    sql = "CREATE DATABASE IF NOT EXISTS 20220428_aula04"
    cursor.execute(sql)
    cursor.execute("use 20220428_aula04 ")

    """
    criar a tabela tb_users com a estrutura que correspondem ao arquivo . csv
    essa tabela tera que ter um campo chave primaria do tipo int e que seja auto increment
    
    o script tera que ler o arquivo . csv, e salvar os dados que estao nesse arquivo na tabela tb_users
    
    Criar a tabela no arquivo bootstrap.py
    Criar a lógica de leitura dos dados do arquivo csv e escrita na tabela no arquivo
    main.py
    """

    #qualquer comando sql passado como parametro para o metodo cursor.execute
    tb_users= "create table if not exists tb_users" \
              "(id int not null auto_increment,e" \
              "mail varchar(200) not null," \
              " name varchar(200) not null," \
              "primary key (id));"
    cursor.execute(tb_users)


