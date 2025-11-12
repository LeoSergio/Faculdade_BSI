from estruturas import (
    StackArray, StackLinkedList,
    QueueArray, QueueLinkedList,
    ListArray, LinkedList
)

print("===== TESTE DE PILHA (ARRAY) =====")
pilha_a = StackArray()
pilha_a.push("A")
pilha_a.push("B")
print("Removido:", pilha_a.pop())  # Esperado: B
print("Removido:", pilha_a.pop())  # Esperado: A

print("\n===== TESTE DE PILHA (LINKED LIST) =====")
pilha_l = StackLinkedList()
pilha_l.push(1)
pilha_l.push(2)
print("Removido:", pilha_l.pop())  # Esperado: 2
print("Removido:", pilha_l.pop())  # Esperado: 1


print("\n===== TESTE DE FILA (ARRAY) =====")
fila_a = QueueArray()
fila_a.enqueue("X")
fila_a.enqueue("Y")
print("Saiu:", fila_a.dequeue())  # Esperado: X
print("Saiu:", fila_a.dequeue())  # Esperado: Y

print("\n===== TESTE DE FILA (LINKED LIST) =====")
fila_l = QueueLinkedList()
fila_l.enqueue(10)
fila_l.enqueue(20)
print("Saiu:", fila_l.dequeue())  # Esperado: 10
print("Saiu:", fila_l.dequeue())  # Esperado: 20


print("\n===== TESTE DE LISTA (ARRAY) =====")
lista_a = ListArray()
lista_a.inserir(0, "Musica A")
lista_a.inserir(1, "Musica B")
lista_a.mostrar()
lista_a.remover("Musica A")
lista_a.mostrar()

print("\n===== TESTE DE LISTA (LINKED LIST) =====")
lista_l = LinkedList()
lista_l.inserir_pos(0, "Música 1")
lista_l.inserir_pos(1, "Música 2")
lista_l.inserir_pos(1, "Música 3")
lista_l.mostrar()
lista_l.remover("Música 3")
lista_l.mostrar()
