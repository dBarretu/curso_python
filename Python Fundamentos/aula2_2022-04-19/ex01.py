#exercicio

#criar um algoritmo que calcula a media de um aluno e mostra uma mensagem, de
#acordo com a media final
#se a media for menor que 5:
#'mostrar a mensagem aluno reprovado
#se a media for maior ou igual a 5 e menor do que 7:
#aluno em recuperacao
# se maior que 7
#aluno aprovado
if __name__ == '__main__':
    pass


    n1= float(input("Insira a nota do primeiro trimestre"))
    n2= float(input("Insira a nota do segundo trimestre"))
    n3= float(input("Insira a nota do terceiro trimestre"))
    media=float


    media= (n1+n2+n3)/3
    print(f"a media do aluno é {media:.2f}")
    #podemos formatar a quantidade de casas decimais mostradas depois do ponto 6.77



    if media <5:
        print("Aluno reprovado ")

    elif media >=5 and media <7  :
        print('Aluno em recuperação')

    else:
        print('Aluno aprovado')







