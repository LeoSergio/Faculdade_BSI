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

