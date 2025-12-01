# Classe auxiliar da Árvore
class Node:
    def __init__(self, cpf, dados):
        self.cpf = cpf
        self.dados = dados
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, cpf, dados):
        if not self.raiz:
            self.raiz = Node(cpf, dados)
        else:
            self._inserir_recursivo(self.raiz, cpf, dados)

    def _inserir_recursivo(self, no, cpf, dados):
        if str(cpf) < str(no.cpf):
            if no.esquerda is None:
                no.esquerda = Node(cpf, dados)
            else:
                self._inserir_recursivo(no.esquerda, cpf, dados)
        elif str(cpf) > str(no.cpf):
            if no.direita is None:
                no.direita = Node(cpf, dados)
            else:
                self._inserir_recursivo(no.direita, cpf, dados)
        else:
            # CPF igual: atualiza dados
            no.dados = dados

    def buscar(self, cpf):
        return self._buscar_recursivo(self.raiz, cpf)

    def _buscar_recursivo(self, no, cpf):
        if no is None:
            return None
        if str(cpf) == str(no.cpf):
            return no.dados
        elif str(cpf) < str(no.cpf):
            return self._buscar_recursivo(no.esquerda, cpf)
        else:
            return self._buscar_recursivo(no.direita, cpf)

    def remover(self, cpf):
        self.raiz = self._remover_recursivo(self.raiz, cpf)

    def _remover_recursivo(self, no, cpf):
        if no is None:
            return no

        if str(cpf) < str(no.cpf):
            no.esquerda = self._remover_recursivo(no.esquerda, cpf)
        elif str(cpf) > str(no.cpf):
            no.direita = self._remover_recursivo(no.direita, cpf)
        else:
            # Caso 1: Nó folha ou com 1 filho
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            
            # Caso 2: Nó com 2 filhos (pega o menor da direita)
            temp = self._min_value_node(no.direita)
            no.cpf = temp.cpf
            no.dados = temp.dados
            no.direita = self._remover_recursivo(no.direita, temp.cpf)
        return no

    def _min_value_node(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual