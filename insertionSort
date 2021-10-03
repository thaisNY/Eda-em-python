#pense em uma pessoa ordenando um baralho de cartas
#vc analisa 2 cartas e ve quem eh menor ent ordena
#dps vc insere uma nova carta e analisa se eh menor que as 2 primeiras
#assim sucessivamente até ordernar todas
#o i começa em 1 por isso j = i - 1,j sempre ponteiro anterior
#caso elemento de j seja maior troca,caso o anterior seja maior troca
#j recebe a chave no final e o i itera
def insertionSort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave

if __name__ == '__main__':
    lista = [4,9,2,1,7,8,1,1,2,7,7,77]
    print(lista)
    print('ordenado\n')
    insertionSort(lista)
    print(lista)
