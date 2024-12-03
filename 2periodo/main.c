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



