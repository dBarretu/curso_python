
# Dicionários

"""
    Um dicionário é uma estrutura de dados do tipo chave: valor
    As chaves só podem ser de alguns tipos específicos, porém os valores podem ser de
qualquer tipo, inclusive outros dicionários

    Dicionários são:
        Iteráveis: Podemos acessar os seus valores sequencialmente dentro de um loop
        Mutáveis: Podemos alterar os seus valores
        Indexáveis: Podemos acessar os valores pelos nomes das chaves
"""

if __name__ == '__main__':

    # Podemos criar um dicionário utilizando a funçã built-in dict()
    my_dict = dict()

    # Podemos criar um dicionário já com os pares chave-valor
    my_dict = {
        'course': "Python",
        'level': "Beginner",
        'started': True,
        'students': [
            "Daniel", "Gabriel", "João Paulo"
        ],
        'info': {
            'start_date': "20220418",
            'end_date': "20220520"
        },
        "rating": 10,
        "mean": 4.9,
        True: "year",
        5.6: "Nao sei",
        #a chave abaixo gerará a exceção type error : unhashable type: list
        [1, 1]: "Vai dar erro"
    }

    #podemos retornar o valor dentro de um dicionario referenciando a sua chave
    print(my_dict)

    # se a chave não existir, é gerada uma exceção KeyError
    #print(my_dict['banana'])

    # podemos utilizar o metodo .get() retorna o valor da chave se essa chave nao existir
    #nao existir ele retorna NONE
    print(my_dict)

    if 'parafuso' in my_dict:
        print(my_dict['parafuso'])

    elif 'chocolate' not in my_dict:
        print('voce nao ganhou um chocolate')

    elif 'course' in my_dict:
        print(f"voce esta no curso de {my_dict['couse']}")

    else:
        print('nada encontrado')

        #adicionamos novos parafusos para chave-valor da seguinte maneira
        my_dict['parafuso']= '10mm'
        my_dict['parafuso'] = '12mm'

        #podemos tambem adicionar ou atualizar com novos itens utilizando o metodo
        #update()
        my_dict.uptade({'parafuso': '14mm', 'observacoes': 'nenhuma'})

        print(my_dict)
#para copiarmos um dicionario no outro, utilizamos o metodo copy()
#valor bizarro my_dict2= my_dict
my_dict2= my_dict.copy()

#podemos apagar pares chave-valor de um dicionario utilizando o metodo .pop()
# se a chave nao existir, podemos passar 

