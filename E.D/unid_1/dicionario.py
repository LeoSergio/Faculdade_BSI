'''
Um jogo mantém um ranking de jogadores
armazenando o nome e a pontuação.
1. Crie um dicionário para representar. o ranking.
2. Insira novos jogadores.
3. Atualize a pontuação de um jogador específico.
4. Encontre o jogador com a maior pontuação.
5. Liste o ranking do maior para o menor.
'''

# 1. Seus dados agora estão em uma LISTA (note os colchetes [])
#    Cada item da lista é um DICIONÁRIO.
jogadores = [
    {"nome": "Arthur", "pontos": 5},
    {"nome": "Vitora", "pontos": 10},
]

# 2. Agora que 'jogadores' é uma lista, você PODE usar o .append()!
#    Você adiciona um novo dicionário à lista.
novo_jogador = {"nome": "Leandro", "pontos": 10}
jogadores.append(novo_jogador)

# 3. Veja o resultado
print(jogadores)
