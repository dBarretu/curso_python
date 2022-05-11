#trabalhando com arquivos .csv
#utilizando o módulo csv

from register import save_user , list_users

import csv

if __name__ == '__main__':

    resposta = int(input("Escolha a opção: 1) Listar 2) Gravar"))

    if resposta == 1:
        with open("clientes.csv", "r") as _file:
            csv_reader = csv.reader(_file, delimiter = ';')
            list_users(csv_file=_file)

    elif resposta == 2:

        # abrimos os arquivos normalmente
        with open("clientes.csv", "a", newline='') as _file:
            #aqui criamos o object csv writer que vaii escrever
            #os dados no arquivo da maneira que definirmos
            csv_writer = csv.writer(_file, delimiter=';')


            payload = {
                "name" : 'daniela',
                "birth_date" : "215451",
                'csv_file': csv_writer
            }

            save_user(**payload)

