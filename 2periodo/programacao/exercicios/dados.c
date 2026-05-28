/*
O algoritimo esta convertendo tudo, deveria converter apenas
letras e digitos

O tamanho do "SHIFT"/k esta fixo
Não trata acentos
Não indexa o alfabeto de A até Z;

criar uma função para corrigir os erros


*/
#include <stdio.h>
#include <stdlib.h>


int main(void){
    int k;
    char letra;
    FILE *fp1,*fp2;
    
    fp1 = fopen("original.txt", "rt");//, leio fgetc
    fp2 = fopen("codificado.txt", "wt"); //escrevo fputc

    letra = fgetc(fp1);
    k=1; //inicializador;
    while (letra != EOF){
        letra = letra + k;
        fputc(letra, fp2);
        letra = fgetc(fp1);

}
    fclose(fp1);
    fclose(fp2);

    return 0;
}

int valida(){
    
}