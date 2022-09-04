from tkinter import N


lista_de_dados = [35, 37, 36, 34, 38, 35, 37, 37,
                  33, 36, 38, 37, 35, 37, 34, 33, 37,  
                  36, 35, 38, 36, 35, 36, 37, 38, 39,
                  37, 37, 36, 37, 33, 37, 35, 37, 39]

def EncontrarAmostragem(lista):
    amostragem = []

    for a in lista:
        if(a not in amostragem):
            amostragem.append(a)

    return amostragem

print(EncontrarAmostragem(lista_de_dados))

def ContarNumerodeVezesQueAparece(lista):
    lista_com_contagem = []

    for n in lista:
        lista_com_contagem.append(0)

    count = 0

    for o in lista:

        for n in lista_de_dados:
            if(o== n):
                lista_com_contagem[count] +=1

        count +=1

    return lista_com_contagem

#guarda as informacoes em variaveis e mostra em tela
lista_de_amostras = EncontrarAmostragem(lista_de_dados)

print(f"Lista de amostras -> {lista_de_amostras}" )

lista_com_contagens = ContarNumerodeVezesQueAparece(lista_de_amostras)

print(f"Lista de contagens -> {lista_com_contagens}")

#agora encontrar a MODA
def ContarNumeroDeVezesQueAparece(lista):

    def EncontraModa(lista1,lista2):
        valorInicial = lista2[0]
        indiceModa = 0
        count = 0

        for n in lista2:
            if(valorInicial <= n):
                valorInicial= n
                indiceModa = count
    
        count += 1

    return lista1[indiceModa]
print("Moda : {moda}")

