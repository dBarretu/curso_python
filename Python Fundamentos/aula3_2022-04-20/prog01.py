
"""
list comprehension
list comprehension é uma maneira mais "enxuta" para criar listas

"""

if __name__ == '__main__':

    numbers_list = []

    for number in range(101):

        #se o resto da divisao de number por 2 for igual a 1
        if number %2  ==1:

            #adiciona esse numero na lista de numero impares
            numbers_list.append(number)

        print(numbers_list)

        #list comprehension

    print([number for number in range(101) if number % 2 == 1])
    print(numbers_list)

    #dicionary comprehension
    dict_list = {number: True for number in range(10)}

    print(numbers_list)
    print(dict_list)
