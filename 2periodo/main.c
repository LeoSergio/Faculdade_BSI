#include <stdio.h>
#include <stdlib.h>

int main(void) {
   FILE *fp;
 char linha[255];
 printf("Exemplo com Arquivos Texto\n");
 fp = fopen("cliente.txt","rt");
 if (fp == NULL){
 printf("Erro na criacao do arquivo\n!");
 exit(1);
 }
 while (fscanf(fp,"%[^\n]",linha) == 1) {
 printf("%s\n",linha);
 fgetc(fp);
 }
 fclose(fp);
 return 0;
}


int main() {
        int op;

    printf("Iniciando o programa...\n");

    do {
        op = tela_main(); // Supomos que tela_main exibe o menu e retorna uma opção válida ou inválida
        if (op >= 0 && op <= 6) {  // Verifica se a opção está no intervalo esperado
            switch (op) {
                case 1:
                    tela_mod_cliente();
                    break;
                case 2:
                    tela_mod_vendas();
                    break;
                case 3:
                    tela_mod_func();
                    break;
                case 4:
                    tela_mod_prod();
                    break;
                case 5:
                    tela_mod_relat();
                    break;
                case 6:
                    tela_info_proj();
                    break;
                case 0:
                    printf("Saindo...\n");
                    break;
            }
        } else {
            printf("Opção inválida! Tente novamente.\n");
        }
    } while (op != 0);

    printf("FIM DO PROGRAMA!\n");
    return 0;
}






int tela_main(void){    
    int op;
    printf("\n");
    printf("===========================================================\n");
    printf("=====                SIG-Building                     =====\n");
    printf("===========================================================\n");
    printf("=====    Sistema de gestão de material de construção  =====\n");
    printf("===========================================================\n");
    printf("=====                [1] - Clientes                   =====\n");
    printf("=====                [2] - Vendas                     =====\n");
    printf("=====                [3] - Funcionário                =====\n");
    printf("=====                [4] - Produto                    =====\n");
    printf("=====                [5] - Relatório                  =====\n");
    printf("=====                [6] - Sobre o Projeto            =====\n");
    printf("=====                [0] - Sair                       =====\n");
    printf("===========================================================\n");
    printf("Sua Escolha: --> ");

    if (scanf("%d", &op) != 1) {  // Valida se a entrada foi um número
        while (getchar() != '\n');  // Limpa o buffer de entrada
        return -1;  // Retorna um valor fora do intervalo esperado para indicar erro
    }

    return op;
}

