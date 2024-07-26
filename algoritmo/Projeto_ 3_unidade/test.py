import validacao
import modulo1
import modulo2

def exibir_dieta(cpf):   
    if cpf in modulo1.cadastro:
        name_dieta = input('Digite o nome da dieta: ')
        name_dieta_validado = validacao.valida_nome(name_dieta)

        if name_dieta_validado:
            if cpf in modulo2.dieta and modulo2.dieta[cpf][0].upper() == name_dieta_validado:
                print('NOME DA DIETA: ', modulo2.dieta[cpf][0])
                print('ALERGIA: ', modulo2.dieta[cpf][1])
                print('OBJETIVO: ', modulo2.dieta[cpf][2])
                print('HORARIO: ', modulo2.dieta[cpf][3])
                input('Tecle <ENTER> para continuar...')
            else:
                print('Dieta não encontrada ou não cadastrada para este CPF.')
        else:
            print('Nome da dieta inválido.')
    else:
        print('CPF não cadastrado no sistema.')
        

