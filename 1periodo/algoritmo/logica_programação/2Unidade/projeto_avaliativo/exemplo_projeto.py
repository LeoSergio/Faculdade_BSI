'''def menu_principal():
    print("\n### MENU PRINCIPAL ###")
    print("1 - Perfil do Paciente")
    print("2 - Planos de Atendimento")
    print("3 - Objetivos do Paciente")
    print("4 - Plano de Dietas Personalizados")
    print("5 - Finalizar Consulta")
    escolha = input("Escolha uma opção (1-5): ")
    return escolha

# Função principal para executar o programa
def main():
    print("Bem-vindo ao programa de gestão de pacientes!")

    # Inicializar o perfil do paciente
    perfil = []

    while True:
        opcao = menu_principal()

        if opcao == '1':
            perfil = criar_perfil()
        elif opcao == '2':
            plano = selecionar_plano()
        elif opcao == '3':
            objetivos = definir_objetivos()
        elif opcao == '4':
            plano_dietas = gerar_plano_dietas()
        elif opcao == '5':
            print("Consulta finalizada. Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()'''