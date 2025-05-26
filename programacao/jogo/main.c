/*
3 chances
fazer uma matriz 3x3
Em um tabuleiro estático 3 x 3
⦿ Em um tabuleiro dinâmico 4 x 4
⦿ Em um tabuleiro dinâmico m x m, onde o valor
de m é definido pelo usuário




#include <stdio.h>
#include <stdlib.h>

void preencheMatriz(int, int, int*);
void exibeMatriz(int, int, int*);

int main(void) {
    int m, n, *mat;
    printf("Informe tamanho da matriz: \n");
    printf("Linhas: ");
    scanf("%d", &m);
    printf("Colunas: ");
    scanf("%d", &n);
    mat = (int*) malloc(m*n*sizeof(int));
    printf("\nInforme os elementos da matriz\n");
    preencheMatriz(m, n, mat);
    printf("\nMatriz Lida\n");
    exibeMatriz(m, n, mat);
    free(mat);
    return 0;
}

void preencheMatriz(int m, int n, int *v) {
    int k;
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
        printf("mat[%d][%d]: ", i+1, j+1);
        k = i*n + j;
        scanf("%d", &v[k]);
        }
    }
}
void exibeMatriz(int m, int n, int *v) {
    for (int k=0; k<m*n; k++) {
    printf("%3d", v[k]);
    if ((k+1)%n==0) {
    printf("\n");
    }
 }
}


#include <stdlib.h>
#include <stdio.h>

char tab[3][3] = " '_' '_' '_';
                   '_' '_' '_';
                   '_' '_' '_' ";


void mostra_tab(char*tab, int tam){
    lsystem("clear");
    printf("Jogo da Doninha \n\n");
    for (int i=0; i< tam; i++){
        for (int j=0; j<tam; j++){
            printf("%c\t, tab[i][j]");
        }
        printf("\n");
    }
}



*/


// Imports




