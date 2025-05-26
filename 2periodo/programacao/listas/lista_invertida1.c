// https://replit.com/@flaviusgorgonio/ExemploDeListaInvertidac

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* duplica(char*);
static char* lelinha(void);

typedef struct cliente Cliente;

struct cliente {
  int codigo;
  char* nome;
  Cliente* prox;
} ;

int main(void) {
  Cliente* clnt;
  Cliente* lista;
  
  lista = NULL;
  
  // Criando o primeiro cliente
  clnt = (Cliente*) malloc(sizeof(Cliente));
  clnt->codigo = 1;
  printf("Nome do Cliente %d: ", clnt->codigo);
  clnt->nome = lelinha();
  clnt->prox = lista;
  lista = clnt;

  // Criando o segundo cliente
  clnt = (Cliente*) malloc(sizeof(Cliente));
  clnt->codigo = 2;
  printf("Nome do Cliente %d: ", clnt->codigo);
  clnt->nome = lelinha();
  clnt->prox = lista;
  lista = clnt;

  // Criando o terceiro cliente
  clnt = (Cliente*) malloc(sizeof(Cliente));
  clnt->codigo = 3;
  printf("Nome do Cliente %d: ", clnt->codigo);
  clnt->nome = lelinha();
  clnt->prox = lista;
  lista = clnt;

  // Exibindo os clientes
  printf("\nLista de Clientes\n");
  clnt = lista;
  while (clnt != NULL) {
    printf("Endereço atual: %p\n", clnt);
    printf("Código: %d\n", clnt->codigo);
    printf("Nome: %s\n", clnt->nome);
    printf("Endereço do próximo: %p\n\n", clnt->prox);

    clnt = clnt->prox;
  }
  // Limpando a memória
  clnt = lista;
  while (lista != NULL) {
    lista = lista->prox;
    free(clnt->nome);
    free(clnt);
    clnt = lista;
  }
  printf("Fim do programa\n");
  return 0;
}

static char* lelinha(void) {
  char linha[255];
  scanf(" %250[^\n]", linha);
  return duplica(linha);
}

char* duplica(char* s) {
  int n = strlen(s) + 1;
  char* d = (char*) malloc(n*sizeof(char));
  strcpy(d, s);
  return d;
}
