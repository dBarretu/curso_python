# tuplas

if __name__ == '__main__':
#podemos criar uma tupla de 2 maneiras

    my_tpl = tuple([1, 2])
    print(my_tpl)

    my_tpl = (1, 2, 3, 4, 5)
    print(my_tpl)

    # tuplas sao indexaveis ou seja, podemos acessar os seus valores a partir
    # de um indice
    print(my_tpl[0])
    print(my_tpl[2:])

    # tuplas sao imutaveis ou seja  nao conseguimos altera-las depois de criadas
    # my_tpl[0] = 1000

    # pra contornar isso, podemos transformar uma tupla em uma lista alterar essa
    # nova lista e gerar uma nova tupla a partir dessa nova lista
    my_list = list(my_tpl)
    print(my_list)
    my_list.apprend(1000)
    my_tpl = tuple(my_list)
    print(my_tpl)

    # set
    my_set = {1, 2, 3, 4, 5, 1, 2, 3, 1, 2}
    print(my_set)


