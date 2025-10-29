#include <stdio.h>
#include <stdlib.h>

struct lista {
	int info;
	struct lista *prox;
};

typedef struct lista Lista;

Lista* lst_cria(void){
	return NULL;
}

Lista* lst_insere(Lista *l, int i){
	Lista *novo = (Lista*) malloc(sizeof(Lista));
	novo->info = i;
	novo->prox = l;
	return novo;
}

void lst_imprime(Lista *l){
	Lista *p;
	for (p = l; p != NULL; p = p->prox){
		printf("%d\t",p->info);
	}
	printf("\n\n");
}

int lst_vazia(Lista *l){
	return (l == NULL);
}

Lista* lst_busca(Lista *l, int v){
	Lista *p;
	for (p = l; p != NULL; p = p->prox){
		if (p->info == v)
			return p;
	}
	return NULL;
}

Lista* lst_retira(Lista *l, int v){
	Lista *ant = NULL;
	Lista *p = l;
	
	while(p != NULL && p->info != v){
		ant = p;
		p = p->prox;
	}
	
	if (p == NULL)
		return l;
		
	if (ant == NULL)
		l = p->prox;
	else
		ant->prox = p->prox;
		
	free(p);
	return l;
}

void lst_libera(Lista *l){
	Lista *p = l;
	while (p != NULL){
		Lista *t = p->prox;
		free(p);
		p = t;
	}
}

void lst_imprime_rec(Lista *l){
	if (l != NULL){
		lst_imprime_rec(l->prox);
		printf("%d\t",l->info);
		
	}
}

Lista* lst_insere_final(Lista *l, int i){
  Lista *p = l;
	Lista *novo = (Lista*) malloc(sizeof(Lista));
	novo->info = i;
	novo->prox = NULL;
  if (l == NULL) {
    l = novo;
  } else {
    while (p->prox != NULL) {
      p = p->prox;
    }
    p->prox = novo;
  }
  return l;
}

Lista* lst_insere_ordem(Lista *l, int i){
	Lista *novo = (Lista*) malloc(sizeof(Lista));
	novo->info = i;
  if (l == NULL) {
    l = novo;
    l->prox = NULL;
  } else if (novo->info < l->info) {
    novo->prox = l;
    l = novo;
  } else {
    Lista* ant = l;
    Lista* atu = l->prox;
    while ((atu != NULL) && (atu->info < novo->info)) {
      ant = atu;
      atu = atu->prox;
    }
    ant->prox = novo;
    novo->prox = atu;
  }
  return l;
}