if __name__ == '__main__':
    pass

    """
    while é uma outra estrutura de repetição em python. o bloco de codigo sera executado 
    enquanto a condicao for verdadeira
    """

    number= None
    numbers_list=[]

#enquanto o numero informado no terminal for diferente de zero o bloco de codigo
#abaixo sera executado
    while number != 0:
        number = int(input("informe um numero:"))

        # o metodo append() adiciona um novo item no final da lista
        numbers_list.append(number)
        """
        as regras das instruões break, continue e else do for, se aplicam ao laço while
        """
        print(sum(numbers_list))

