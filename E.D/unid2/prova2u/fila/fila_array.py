class QueueArray:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        return None

    def is_empty(self):
        return len(self.data) == 0


fila_impressao = QueueArray()
fila_impressao.enqueue("Arquivo1.pdf")
fila_impressao.enqueue("Arquivo2.png")
fila_impressao.enqueue("Arquivo3.docx")

print("Imprimindo:", fila_impressao.dequeue())
print("Imprimindo:", fila_impressao.dequeue())
