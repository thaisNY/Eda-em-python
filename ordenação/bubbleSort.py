#compara 1 elemento da pos i com o proximo caso seja menor troca
#o elemento i eh comparado com todos os elementos da lista
#ao achar um elemento menor a troca eh feita
#a cada final da primeira iteração de j, o menor elemento vai estar no final da lista
#são feitas n - 1 trocas, sendo n o tamanho da lista
def bubbleSort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
            i+= 1

if __name__ == '__main__':
    lista = [4,9,2,1,7,8,1,1,2,7,7,77]
    print(lista)
    print('ordenado\n')
    bubbleSort(lista)
    print(lista)

