# A CLASSE Hash (usa a árvore)
from arvore_binaria import ArvoreBinaria

class HashBinaria:
    def __init__(self, tamanho=100): # Tamanho menor para FORÇAR colisões e usar a árvore
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho
        
        # Inicializa cada posição com uma árvore vazia
        for i in range(self.tamanho):
            self.tabela[i] = ArvoreBinaria()

    def _hash(self, chave):
        chave_limpa = int(str(chave).replace('.', '').replace('-', ''))
        return chave_limpa % self.tamanho

    def inserir(self, cpf, dados):
        indice = self._hash(cpf)
        self.tabela[indice].inserir(cpf, dados)

    def buscar(self, cpf):
        indice = self._hash(cpf)
        return self.tabela[indice].buscar(cpf)

    def remover(self, cpf):
        indice = self._hash(cpf)
        self.tabela[indice].remover(cpf)