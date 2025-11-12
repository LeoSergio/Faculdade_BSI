class ListArray:
    def __init__(self):
        self.data = []

    def inserir(self, pos, valor):
        self.data.insert(pos, valor)

    def remover(self, valor):
        if valor in self.data:
            self.data.remove(valor)

    def mostrar(self):
        print("Playlist:", self.data)


playlist = ListArray()
playlist.inserir(0, "Música A")
playlist.inserir(1, "Música B")
playlist.inserir(1, "Música C")
playlist.mostrar()
playlist.remover("Música B")
playlist.mostrar()
