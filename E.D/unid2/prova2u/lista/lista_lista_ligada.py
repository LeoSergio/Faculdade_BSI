class LinkedList:
    def __init__(self):
        self.head = None

    def inserir_inicio(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo

    def inserir_pos(self, pos, valor):
        if pos == 0:
            self.inserir_inicio(valor)
            return

        atual = self.head
        count = 0
        while atual and count < pos - 1:
            atual = atual.next
            count += 1

        if not atual:
            return

        novo = Node(valor)
        novo.next = atual.next
        atual.next = novo

    def remover(self, valor):
        if self.head and self.head.value == valor:
            self.head = self.head.next
            return

        atual = self.head
        while atual.next and atual.next.value != valor:
            atual = atual.next

        if atual.next:
            atual.next = atual.next.next
