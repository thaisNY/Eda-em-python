from node import Node
#Métodos
#inserir na fila
#remover na fila
#observar o topo da fila

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        #insiri o elemento na fila
        #a inserção vai modificar o último
        #existe um unico caso que o primeiro elem vai ser modificado, quando a pilha ta vazia
        node = Node(elem)

        if self.last is None:
            self.last = node
        else:
            self.last.next = node #avisa ao ultimo que alguem chegou atras dele
            self.last = node #define o elem incluido como ultimo elem

        if self.first is None: #se a pilha ta vazia,o 1 eh o cara que acabou de chegar
            self.first = node

        self._size = self._size + 1

    def pop(self):
        #remove o elemento do topo da fila
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        print('The queue is empety')
    def peek(self):
        #retorna o topo sem remover
        if self._size > 0:
            elem = self.first.data
            return elem
        print('The queue is empety')
    def __len__(self):
        #exibi o tamanho da fila
        return self._size
    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empety Queue"

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    fila = Queue()
    #print(fila)
    fila.push(5)
    print(fila)
    fila.push(21)
    fila.push("Thais")
    fila.push(True)
    fila.push(42)
    print(fila)
    fila.pop()
    print(fila)
    print(fila.peek())
    print(fila)
    fila.push(5)
    print(fila)
    fila.pop()
    fila.pop()
    fila.pop()
    fila.pop()
    print(fila)
    fila.pop()
    print(fila)
    fila.pop()
    print(len(fila))
    fila.push(42)
    print(len(fila))

