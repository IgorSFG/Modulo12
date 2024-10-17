#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 10  // Define o tamanho máximo da pilha

// Estrutura da Pilha
typedef struct {
    int itens[MAX];
    int topo;
} Pilha ;

// Inicializa a pilha
void inicializar(Pilha *p) {
    (*p).topo = -1;
    //p->topo = -1;
}

// Verifica se a pilha está cheia
int estaCheia(Pilha *p) {
    return (*p).topo == MAX - 1;
    //return p->topo == MAX - 1;
}

// Verifica se a pilha está vazia
int estaVazia(Pilha *p) {
    return (*p).topo == -1;
    //return p->topo == -1;
}

// Empilha um elemento
void empilhar(Pilha *p, int valor) {
    if (estaCheia(p)) {
        printf("Erro: Pilha está cheia.\n");
    } else {
        ++((*p).topo);
        (*p).itens[(*p).topo] = valor;
        //p->itens[++(p->topo)] = valor;
        printf("%d empilhado.\n", valor);
    }
}

// Desempilha um elemento
int desempilhar(Pilha *p) {
    if (estaVazia(p)) {
        printf("Erro: Pilha está vazia.\n");
        return -1;  // Retorna um valor inválido para indicar erro
    } else {
        //return p->itens[(p->topo)--];
        return (*p).itens[((*p).topo)--];
    }
}

// Exibe o topo da pilha
int topo( Pilha *p) {
    if (estaVazia(p)) {
        printf("Erro: Pilha está vazia.\n");
        return -1;
    } else {
        return p->itens[p->topo];
    }
}

void exibePilha(Pilha p){
    if(estaVazia(&p)){
        printf("Pilha Vazia!\n");
        return;
    }
    int i;
    for(i = 0; i <= p.topo; i++){
        printf("Posicao[%i]: %i\n",
               i,
               p.itens[i]);
    }
}

int tamanhoDaPilha(Pilha p){
    return p.topo+1;
}
// Função principal
int main() {
    Pilha p;
    inicializar(&p);
    char opcao[MAX];
    int continuar = 1;
    do{ 
        printf("\nDigite um número ou operação (+ ou sair): ");
        scanf("%s", opcao);

        if(!strcmp(opcao, "sair")) continuar = 0;
        else if(!strcmp(opcao, "+")){
            if(tamanhoDaPilha(p) > 1){
                int numero1, numero2, res;
                numero1 = desempilhar(&p);
                numero2 = desempilhar(&p);
                res = numero1 + numero2;
                empilhar(&p, res);
            } else {
                printf("Não tem itens suficiente...\n");
            }
            exibePilha(p);
        }
        else{
            int numero;
            numero = atoi(opcao);
            empilhar(&p, numero);
            exibePilha(p);
        }
    }while(continuar);
    return 0;
}