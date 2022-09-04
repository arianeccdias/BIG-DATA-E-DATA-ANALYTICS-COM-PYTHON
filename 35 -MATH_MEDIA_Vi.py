lista_de_dados = [28, 30, 29, 31, 32, 33, 34]

#funcao que retorna o valor da media
def media(lista):

    #inicializando as variaveis
    total_das_somatorias = 0
    n_de_dados = 0

    # faz a somatoria e conta o numero de dados
    for n in lista:
        total_das_somatorias += n
        n_de_dados +=1

    #retorna a somatoria divida pelo numero de dados
    return total_das_somatorias/n_de_dados


#mostra em tela o resultado
print(media(lista_de_dados))


    
