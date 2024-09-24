#include <stdio.h>
char nome[21];
float alt;
float peso;
float imc;

void main(void){   
    printf("Qual o seu nome? ");
    scanf("%c", &nome);
    printf("Digite sua Altura: ");
    scanf("%f",alt);
    printf("Qual o seu peso? ");
    scanf("%f",&peso);

    printf("Seu imc é: %.f",imc);
    
    
// peso / altura**2
}