from nodee import Node
no1 = Node(5)
no2 = Node(9)
no1.data
print(no1.data)
no2.data
print(no2.data)
print(no1.next) #None
no1.next = no2
print(no2)
print(no1.next.data)
