import validacao
nome = input('Qual o nome da Dieta? --> ')
nome = validacao.valida_nome(nome)
if nome:
    print(nome)
    print('INFORMAÇÕES EXCLUIDA COM SUCESSO: ')
    function.cad_dieta()
    option = input('Digite outra opção: ')