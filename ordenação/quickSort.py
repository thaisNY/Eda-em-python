def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = particion(lista, inicio, fim)
        quicksort(lista,inicio, p - 1)
        quicksort(lista, p + 1, fim)
def particion(lista, inicio, fim):
    i = inicio
    pivot = lista[fim]
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j],lista[i] = lista[i],lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

if __name__ == '__main__':
    lista = [4,9,2,1,7,8,1,1,2,7,7,77]
    print(lista)
    print('ordenado\n')
    quicksort(lista)
    print(lista)







