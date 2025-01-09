#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct amigo Amigo;

struct amigo {
  int codigo;
  char* nome;
  char* fone;
  Amigo* prox;
} ;

char* duplica(char*);
static char* lelinha(void);

Amigo* cadastra_amigo(Amigo*);
Amigo* pesquisa_amigo(Amigo*);
void altera_amigo(Amigo*);
Amigo* exclui_amigo(Amigo*);
void exibe_amigo(Amigo*);
void exibe_lista(Amigo*);
Amigo* limpa_lista(Amigo*);
char menu(void);


int main(void) {
  Amigo* lista;
  Amigo* am;
  char op;

  lista = NULL;

  do {
    op = menu();
    switch(op) {
        case '1' :  lista = cadastra_amigo(lista);
                    break;
        case '2' :  am = pesquisa_amigo(lista);
                    exibe_amigo(am);
                    break;
        case '3' :  altera_amigo(lista);
                    break;
        case '4' :  lista = exclui_amigo(lista);
                    break;
        case '5' :  exibe_lista(lista);
                    break;
    }
  } while(op != '0');

  lista = limpa_lista(lista);
  printf("Fim do programa\n");
  return 0;
}


Amigo* cadastra_amigo(Amigo* lista) {
    Amigo* am;

    am = (Amigo*) malloc(sizeof(Amigo));
    printf("Nome do Amigo: ");
    am->nome = lelinha(); getchar();
    printf("Fone do Amigo: ");
    am->fone = lelinha(); getchar();
    am->prox = NULL;

    if (lista == NULL) {
        return am;
    } else {
        Amigo* ultimo;
        ultimo = lista;
        while (ultimo->prox != NULL) {
            ultimo = ultimo->prox;
        }
        ultimo->prox = am;
        return lista;
    }
}


void exibe_lista(Amigo* lista) {
    Amigo* am;

    printf("\nLista de Amigos\n");
    printf("===== == ======\n");
    am = lista;
    while (am != NULL) {
        printf("Nome: %s\n", am->nome);
        printf("Fone: %s\n", am->fone);
        printf("\n");
        am = am->prox;
    }
    printf("\nTecle ENTER para continuar...\n");
    getchar();
}


void altera_amigo(Amigo* lista) {
    // Falta desenvolver
}


Amigo* exclui_amigo(Amigo* lista) {
    // Falta desenvolver
    return lista;
}

void exibe_amigo(Amigo* lista) {
    // Falta desenvolver
}

Amigo* pesquisa_amigo(Amigo* lista) {
    Amigo* am = NULL;
    // Falta desenvolver
    return am;
}

Amigo* limpa_lista(Amigo* lista) {
    Amigo* am;

    am = lista;
    while (lista != NULL) {
        lista = lista->prox;
        free(am);
        am = lista;
    }
    return lista;
}


char menu(void) {
    char op;
    system("cls||clear");
    printf("=== Lista Dinâmica ===\n\n");
    printf("=== 1. Cadastrar amigo ===\n");
    printf("=== 2. Pesquisar amigo ===\n");
    printf("=== 3. Editar amigo ===\n");
    printf("=== 4. Excluir amigo ===\n");
    printf("=== 5. Exibir lista ===\n");
    printf("=== Escolha sua opção: ");
    scanf("%c", &op);
    getchar();
    return op;
}


static char* lelinha(void) {
  char linha[255];
  scanf(" %26[^\n]", linha);
  return duplica(linha);
}


char* duplica(char* s) {
  int n = strlen(s) + 1;
  char* d = (char*) malloc(n*sizeof(char));
  strcpy(d, s);
  return d;
}
