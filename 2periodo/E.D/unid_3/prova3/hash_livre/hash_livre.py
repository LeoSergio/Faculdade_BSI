# A CLASSE (Lógica pura)
class HashLivre:
    def __init__(self, tamanho=15013): # Tamanho primo > 10.000 para evitar muitos clusters
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho
        self.quantidade = 0

    def _hash(self, chave):
        # Remove caracteres não numéricos do CPF se houver e converte
        chave_limpa = int(str(chave).replace('.', '').replace('-', ''))
        return chave_limpa % self.tamanho

    def inserir(self, cpf, dados):
        indice = self._hash(cpf)
        indice_inicial = indice

        while self.tabela[indice] is not None:
            # Se já existe o CPF (atualização), sobrescreve e retorna
            if self.tabela[indice][0] == cpf:
                self.tabela[indice] = (cpf, dados)
                return
            
            # Sondagem Linear: tenta o próximo
            indice = (indice + 1) % self.tamanho
            
            # Se deu a volta completa, tabela cheia (teoricamente não ocorre aqui se tamanho > N)
            if indice == indice_inicial:
                raise Exception("Tabela Hash cheia!")

        # Encontrou espaço vazio
        self.tabela[indice] = (cpf, dados)
        self.quantidade += 1

    def buscar(self, cpf):
        indice = self._hash(cpf)
        indice_inicial = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice][0] == cpf:
                return self.tabela[indice][1] # Retorna os dados
            
            indice = (indice + 1) % self.tamanho
            if indice == indice_inicial:
                return None
        return None

    def remover(self, cpf):
        indice = self._hash(cpf)
        indice_inicial = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice][0] == cpf:
                self.tabela[indice] = None # Remoção simples (pode exigir rehash em implementações complexas)
                self.quantidade -= 1
                return True
            
            indice = (indice + 1) % self.tamanho
            if indice == indice_inicial:
                return False
        return False