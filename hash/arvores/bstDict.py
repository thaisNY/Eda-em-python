root = {}
op = 0
def empety(aux):
    if len(aux.values()) <= 0:
        return True
    else:
        return False

def insertTree(aux, num):
    if empety(aux) :
        aux = {"num": num, "left": {}, "right": {}}   #se tiver vazio insere como raiz, salva no aux

    elif num < aux["num"] :
        aux["left"] = insertTree(aux["left"], num)  #se n tiver vazio e for menor que raiz insere a esq
    else:
        aux["right"] = insertTree(aux["right"], num) #se n tiver vazio e for maior que a raiz insere a dir
    return aux

def showInOrder(aux):
    if not empety(aux):
        showInOrder(aux["left"]) #{"num": 4, "left": {}, "right": {}},que passa para aux // chama de nv o da esq que é {} n entra no if ent sai da recursao
        print(aux["num"], end=" ") #impimi 4
        showInOrder(aux["right"]) #chama o da direita que eh {} sai da recursao fim da primeira chamada {"num": 4, "left": {}, "right": {}} apaga
        #imprimi o 6
        #chama o da direita {{"num": 10, "left": {}, "right": {}}, que passa para aux//chama da esq que eh {} sai da recursao //imprimi 10 //chama da direita {} sai da recursao  fim da 2 chamada  {{"num": 10, "left": {}, "right": {}} se apaga
        #4 6 10

def showPairs(aux):
    if not empety(aux):
        showPairs(aux["left"])
        if aux["num"] % 2 == 0:
            print(aux["num"], end=" ")
        showPairs(aux["right"])

#root = insertTree(root, 6)   #{"num": 6, "left": {}, "right": {}}
#root = insertTree(root, 4)   #{"num": 6, "left": {{"num": 4, "left": {}, "right": {}}}, "right": {}}
#root = insertTree(root, 10)  #{"num": 6, "left": {{"num": 4, "left": {}, "right": {}}, "right": {{"num": 10, "left": {}, "right": {}}}
#print(root)
#showInOrder(root)
#print(root)

while op != 5:
    print('Binary tree options menu')
    print('1 - Insert numbers')
    print('2 - Consult the pairs')
    print('3- Consult the binary tree in order')
    print('4- Empety the tree')
    print('5- Exit')
    op = int(input('Type your option'))
    if op < 1 and op > 5:
        print('Invalid option \n Try again \n')
        continue
    elif op == 1:
        counter = 0

        while counter < 10:
            root = insertTree(root, int(input('Type a number: ')))
            counter += 1

    elif op == 2:
        if empety(root):
            print('Empety tree')
            continue
        else:
            showPairs(root)
            continue
    elif op == 3:
        if empety(root):
            print('Empety tree')
            continue
        else:
            showInOrder(root)
            continue
    elif op == 4:
        if not empety(root):
            root.clear() #apaga td key value do dict
            continue
        else:
            print('Empety tree')
            continue
    elif op == 5:
        break




