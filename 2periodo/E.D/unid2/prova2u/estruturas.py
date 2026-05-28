import time

class Node:
    """Nó para a Lista Ligada."""
    def __init__(self, value):
        self.value = value
        self.next = None

# ======================================================================
# --- PILHA (STACK) ---
# ======================================================================

class StackArray:
    """Implementa a Pilha com Array e redimensionamento manual."""
    def __init__(self, capacidade_inicial=10):
        self.capacidade = capacidade_inicial
        self.dados = [None] * self.capacidade
        self.tamanho = 0
        self.tempos_aumentar = []
        self.tempos_diminuir = []

    def _aumentar_tamanho(self):
        """[Função a ser medida: Aumentar o tamanho físico]"""
        inicio_aumento = time.perf_counter()
        nova_capacidade = self.capacidade * 2
        novos_dados = [None] * nova_capacidade
        for i in range(self.tamanho):
            novos_dados[i] = self.dados[i]
        self.dados = novos_dados
        self.capacidade = nova_capacidade
        fim_aumento = time.perf_counter()
        self.tempos_aumentar.append((fim_aumento - inicio_aumento) * 1000)

    def _diminuir_tamanho(self):
        """[Função a ser medida: Diminuir o tamanho físico]"""
        if self.tamanho > 10 and self.tamanho <= self.capacidade // 4:
            inicio_diminuir = time.perf_counter()
            nova_capacidade = self.capacidade // 2
            novos_dados = [None] * nova_capacidade
            for i in range(self.tamanho):
                novos_dados[i] = self.dados[i]
            self.dados = novos_dados
            self.capacidade = nova_capacidade
            fim_diminuir = time.perf_counter()
            self.tempos_diminuir.append((fim_diminuir - inicio_diminuir) * 1000)

    def push(self, item): # Adicionar
        if self.tamanho == self.capacidade:
            self._aumentar_tamanho()
        self.dados[self.tamanho] = item
        self.tamanho += 1

    def pop(self): # Remover
        if self.is_empty(): return None
        self.tamanho -= 1
        valor = self.dados[self.tamanho]
        self.dados[self.tamanho] = None
        self._diminuir_tamanho()
        return valor

    def is_empty(self):
        return self.tamanho == 0

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, item): # Adicionar
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self): # Remover
        if not self.top: return None
        valor = self.top.value
        self.top = self.top.next
        return valor
    
    def is_empty(self):
        return self.top is None

# ======================================================================
# --- FILA (QUEUE) ---
# ======================================================================

class QueueArray:
    """Implementa a Fila com Array e redimensionamento manual."""
    def __init__(self, capacidade_inicial=10):
        self.capacidade = capacidade_inicial
        self.dados = [None] * self.capacidade
        self.tamanho = 0
        self.tempos_aumentar = []
        self.tempos_diminuir = []

    # _aumentar_tamanho e _diminuir_tamanho são idênticos ao StackArray
    def _aumentar_tamanho(self):
        inicio_aumento = time.perf_counter()
        nova_capacidade = self.capacidade * 2
        novos_dados = [None] * nova_capacidade
        for i in range(self.tamanho):
            novos_dados[i] = self.dados[i]
        self.dados = novos_dados
        self.capacidade = nova_capacidade
        fim_aumento = time.perf_counter()
        self.tempos_aumentar.append((fim_aumento - inicio_aumento) * 1000)

    def _diminuir_tamanho(self):
        if self.tamanho > 10 and self.tamanho <= self.capacidade // 4:
            inicio_diminuir = time.perf_counter()
            nova_capacidade = self.capacidade // 2
            novos_dados = [None] * nova_capacidade
            for i in range(self.tamanho):
                novos_dados[i] = self.dados[i]
            self.dados = novos_dados
            self.capacidade = nova_capacidade
            fim_diminuir = time.perf_counter()
            self.tempos_diminuir.append((fim_diminuir - inicio_diminuir) * 1000)

    def enqueue(self, item): # Adicionar
        if self.tamanho == self.capacidade:
            self._aumentar_tamanho()
        self.dados[self.tamanho] = item
        self.tamanho += 1

    def dequeue(self): # Remover (O(n) - ineficiente!)
        if self.is_empty(): return None
        valor = self.dados[0] # Pega do início
        # Desloca todos os elementos para a esquerda
        for i in range(1, self.tamanho):
            self.dados[i-1] = self.dados[i]
        self.tamanho -= 1
        self.dados[self.tamanho] = None
        self._diminuir_tamanho()
        return valor

    def is_empty(self):
        return self.tamanho == 0

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item): # Adicionar
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
    
    def dequeue(self): # Remover
        if not self.front: return None
        valor = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return valor
    
    def is_empty(self):
        return self.front is None

# ======================================================================
# --- LISTA (LIST) ---
# ======================================================================

class ListArray:
    """Implementa a Lista com Array e redimensionamento manual."""
    def __init__(self, capacidade_inicial=10):
        self.capacidade = capacidade_inicial
        self.dados = [None] * self.capacidade
        self.tamanho = 0
        self.tempos_aumentar = []
        self.tempos_diminuir = []

    # _aumentar_tamanho e _diminuir_tamanho são idênticos ao StackArray
    def _aumentar_tamanho(self):
        inicio_aumento = time.perf_counter()
        nova_capacidade = self.capacidade * 2
        novos_dados = [None] * nova_capacidade
        for i in range(self.tamanho):
            novos_dados[i] = self.dados[i]
        self.dados = novos_dados
        self.capacidade = nova_capacidade
        fim_aumento = time.perf_counter()
        self.tempos_aumentar.append((fim_aumento - inicio_aumento) * 1000)

    def _diminuir_tamanho(self):
        if self.tamanho > 10 and self.tamanho <= self.capacidade // 4:
            inicio_diminuir = time.perf_counter()
            nova_capacidade = self.capacidade // 2
            novos_dados = [None] * nova_capacidade
            for i in range(self.tamanho):
                novos_dados[i] = self.dados[i]
            self.dados = novos_dados
            self.capacidade = nova_capacidade
            fim_diminuir = time.perf_counter()
            self.tempos_diminuir.append((fim_diminuir - inicio_diminuir) * 1000)

    def inserir(self, pos, valor): # Adicionar (O(n))
        if not (0 <= pos <= self.tamanho):
            # Para simplificar, se a posição for inválida, insere no fim
            pos = self.tamanho
            
        if self.tamanho == self.capacidade:
            self._aumentar_tamanho()
            
        # Desloca elementos para a direita
        for i in range(self.tamanho, pos, -1):
            self.dados[i] = self.dados[i-1]
        
        self.dados[pos] = valor
        self.tamanho += 1

    def remover(self, pos): # Remover (O(n))
        if not (0 <= pos < self.tamanho):
            return None # Posição inválida
        
        valor = self.dados[pos]
        
        # Desloca elementos para a esquerda
        for i in range(pos, self.tamanho - 1):
            self.dados[i] = self.dados[i+1]
            
        self.tamanho -= 1
        self.dados[self.tamanho] = None
        self._diminuir_tamanho()
        return valor
        
    def is_empty(self):
        return self.tamanho == 0

class ListLinkedList:
    def __init__(self):
        self.head = None
    
    def inserir_pos(self, pos, valor): # Adicionar
        new_node = Node(valor)
        if pos == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        atual = self.head
        count = 0
        # Percorre até a posição anterior
        while atual.next and count < pos - 1:
            atual = atual.next
            count += 1
        
        new_node.next = atual.next
        atual.next = new_node

    def remover_pos(self, pos): # Remover
        if not self.head:
            return
        
        if pos == 0:
            valor = self.head.value
            self.head = self.head.next
            return valor

        atual = self.head
        count = 0
        # Percorre até a posição anterior
        while atual.next and count < pos - 1:
            atual = atual.next
            count += 1
            
        if atual.next:
            valor = atual.next.value
            atual.next = atual.next.next
            return valor
            
    def is_empty(self):
        return self.head is None