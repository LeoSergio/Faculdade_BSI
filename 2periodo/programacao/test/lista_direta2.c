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
void exibe_lista_direta(Amigo*);
void exibe_lista_inversa(Amigo*);
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
    am->nome = lelinha(); 
    getchar();
    printf("Fone do Amigo: ");
    am->fone = lelinha(); 
    getchar();
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
    printf("Cadastrado com sucesso...");
    getchar();
}


void exibe_lista(Amigo* lista) {
    char ordem;

    printf("Voce deseja exibir a lista em qual ordem?\n");
    printf("1 - Ordem direta\n");
    printf("2 - Ordem inversa\n");
    scanf("%c", &ordem);
    getchar();
    
    printf("\nLista de Amigos\n");
    printf("===== == ======\n");
    
    if (ordem == '1') {
        exibe_lista_direta(lista);
    } else if (ordem == '2'){
        if (lista != NULL) {
            exibe_lista_inversa(lista);
        }
        
    }
    
    printf("\nTecle ENTER para continuar...\n");
    getchar();
}


void exibe_lista_direta(Amigo* am) {

    while (am != NULL) {
        printf("Nome: %s\n", am->nome);
        printf("Fone: %s\n", am->fone);
        printf("\n");
        am = am->prox;
    }
}


void exibe_lista_inversa(Amigo* am) {

    if (am->prox != NULL) {
        exibe_lista_inversa(am->prox);
    }
    printf("Nome: %s\n", am->nome);
    printf("Fone: %s\n", am->fone);
    printf("\n");
}


void altera_amigo(Amigo* lista) {
    Amigo* am;

    am = pesquisa_amigo(lista);
    if (am == NULL) {
        printf("Esta pessoa nao esta cadastrada!\n");
    } else {
        printf("Nome: %s\n", am->nome);
        printf("Fone: %s\n", am->fone);
        printf("\nInforme os novos dados:\n");
        printf("Nome do Amigo: ");
        free(am->nome);
        am->nome = lelinha(); 
        getchar();
        printf("Fone do Amigo: ");
        free(am->fone);
        am->fone = lelinha(); 
        getchar();
    }
    // Falta desenvolver
    printf("\n");
    printf("Tecle ENTER para continuar...");
    getchar();
}


Amigo* exclui_amigo(Amigo* lista) {
    Amigo* am;

    am = pesquisa_amigo(lista);
    if (am == NULL) {
        printf("Esta pessoa nao esta cadastrada!\n");
        getchar();
    } else {
        if (lista->prox == NULL) {
            free(am->nome);
            free(am->fone);
            free(am);
            lista = NULL;
        } else {
            Amigo* ant;
            ant = lista;
            if (am == ant) {
                lista = lista->prox;
            } else {
                while ((ant != NULL) && (ant->prox != am)) {
                    ant = ant->prox;
                }
                ant->prox = am->prox;
            }
            free(am->nome);
            free(am->fone);
            free(am);
        }
        printf("\n");
        printf("Cadastro excluido com sucesso...");
        getchar();
    }
    return lista;
}

void exibe_amigo(Amigo* lista) {

    if (lista == NULL) {
        printf("Pessoa não existe!\n");
    } else {
        printf("Nome: %s\n", lista->nome);
        printf("Fone: %s\n", lista->fone);
        printf("\n");
    }
    printf("Tecle ENTER para continuar...");
    getchar();
}

Amigo* pesquisa_amigo(Amigo* lista) {
    Amigo* am;
    char nome[100];

    printf("Informe nome a procurar: ");
    scanf("%s", nome);
    getchar();

    am = lista;
    while (am != NULL) {
        if (strcmp(nome, am->nome) == 0) {
            return am;
        } else {
            am = am->prox;
        }
    }
    return NULL;
}

Amigo* limpa_lista(Amigo* lista) {
    Amigo* am;

    am = lista;
    while (lista != NULL) {
        lista = lista->prox;
        free(am->nome);
        free(am->fone);
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
    printf("=== 3. Alterar amigo ===\n");
    printf("=== 4. Excluir amigo ===\n");
    printf("=== 5. Exibir lista ===\n");
    printf("=== 0. Sair do programa ===\n");
    printf("=== Escolha sua opcao: ");
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
