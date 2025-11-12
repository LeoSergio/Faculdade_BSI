class StackArray:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None

    def is_empty(self):
        return len(self.data) == 0

# Exemplo: Undo/Redo
undo = StackArray()
redo = StackArray()

texto = ""

def escrever(novo_texto):
    global texto
    undo.push(texto)
    texto = novo_texto
    print("Texto atual:", texto)

def desfazer():
    global texto
    if not undo.is_empty():
        redo.push(texto)
        texto = undo.pop()
    print("Desfazer →", texto)

def refazer():
    global texto
    if not redo.is_empty():
        undo.push(texto)
        texto = redo.pop()
    print("Refazer →", texto)


escrever("Olá")
escrever("Olá mundo")
desfazer()
refazer()
