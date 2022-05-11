# Importamos o módulo csv no nosso 
# O módulo CSV faz parte da biblioteca padrão do Python
import csv
import uuid

if __name__ == '__main__':

    with open(file="products.csv", mode="a") as _file:

        headers = ['id', 'name', 'price']
        csv_writer = csv.DictWriter(
            _file, fieldnames=headers, delimiter=';'
        )

        # Verifica se o arquivo já existe
        if _file.tell() == 0:
            csv_writer.writeheader()

        # passamos um dicionario como argumento
        csv_writer.writerow({
            'id': str(uuid.uuid4()),
            'name': 'Radio',
            'price': 7.79
        })

        csv_writer.writerows([
            {'id': str(uuid.uuid4()), 'name': 'memory', 'price': 10},
            {'id': str(uuid.uuid4()), 'name': 'alho', 'price':13 }
        ])
