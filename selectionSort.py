#[7,1,5,3,8]
#busco o menor elemento da lista
#compara com o elemento na pos de j
#se o menor for menor do que elemento na pos j troca
#preciso saber o index da menor elemento
#j incrementa a cada comparação
#se cria sublistas ainda não ordenadas apos ordenar os primeiros elemetos
#min_index começa da pos j
#i começa de j

def selectionSort(lista):
    n = len(lista)
    for j in range(n - 1):
        mini_index = j
        for i in range(j,n):
            if lista[i] < lista[mini_index]:
                aux = lista[mini_index]
                lista[mini_index] = lista[i]
                lista[i] = aux

        if lista[mini_index] < lista[j]:
            aux = lista[j]
            lista[j] = lista[mini_index]
            lista[mini_index] = aux

        j += 1
    print(lista)

if __name__ == '__main__':
    #main()
    lista = [7, 1, 5, 3, 8]
    print(lista)
    print("ordenado\n")
    selectionSort(lista)

