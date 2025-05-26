#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* duplica(char*);
static char* lelinha(void);


typedef struct cliente Cliente;
struct cliente{
    int codigo;
    char*nome;
    Cliente*prox;
};

int main (void){
    Cliente*clnt;
    Cliente*lista;
}