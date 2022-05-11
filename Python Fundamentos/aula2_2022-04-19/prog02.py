# Laço for

# Utilizamos o laço de repetição 'for' quando queremos iterar sobre uma sequência, ou seja,
# quando queremos acessar sequencialmente os itens dessa sequência.

if __name__ == '__main__':
        groceries_list = [
            "Laranja",
            "Banana",
            "Abacate",
            "Limão",
            "Manga"
        ]

        print("Itens do mercado")
        for item in groceries_list:
            print(item)

        print("*"*50)

        user_info = {
            'name': 'John',
            'surname': 'Doe',
            'age': 30,
            'gender': 'M',
            'country': 'US'
        }

        # No caso de dicionários, por padrão é retornado o nome da chave.
        # for item in user_info.keys()
        for item in user_info.keys():
            print(item)

        print("*" * 50)

        # Retornando os valores do dicionário:
        for item in user_info.values():
            print(item)

        print("*" * 50)

        #retornando o par chave-valor do dicionario
        for item in user_info.items():

         for item in "Alessandro":
            print(item)

        print("*" * 50)

        #break, continue
        #break interrompe o fluxo de execução e sai do loop

        my_list = [1, 3, 2, 5, 8]

        for number in number_list:
            if number <0:
                break #interrompe o fluxo do for
            print(f"{numer} elevando ao quadrado é igual a {number ** 2}")

            for number in number_list:
                if number <0:
                    continue
                    print(f"{numer} elevando ao quadrado é igual a {number ** 2}")
