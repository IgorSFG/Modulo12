#include <stdio.h>
#include <stdlib.h>

// Estrutura do no da arvore
struct No {
    int valor;
    struct No *esquerda;
    struct No *direita;
};

// Criar um novo no
struct No* novoNo(int valor) {
    struct No* no = (struct No*)malloc(sizeof(struct No));
    no->valor = valor;
    no->esquerda = NULL;
    no->direita = NULL;
    return no;
}

// Inserir um novo no na arvore
struct No* inserir(struct No* raiz, int valor) {
    if (raiz == NULL) {
        return novoNo(valor);  // Se a raiz for nula, insere o primeiro n�
    }

    if (valor < raiz->valor) {
        raiz->esquerda = inserir(raiz->esquerda, valor);  // Inserir na subarvore esquerda
    } else if (valor > raiz->valor) {
        raiz->direita = inserir(raiz->direita, valor);  // Inserir na subarvore direita
    }

    return raiz;
}

// Buscar um valor na arvore
struct No* buscar(struct No* raiz, int valor) {
    if (raiz == NULL || raiz->valor == valor) {
        return raiz;  // Retorna o n� encontrado ou NULL se nao encontrado
    }

    if (valor < raiz->valor) {
        return buscar(raiz->esquerda, valor);  // Buscar na subarvore esquerda
    } else {
        return buscar(raiz->direita, valor);  // Buscar na subarvore direita
    }
}

// Buscar o menor no na arvore
struct No* menorValor(struct No* no) {
    struct No* atual = no;

    // Percorre at� encontrar o n� mais � esquerda (menor valor)
    while (atual && atual->esquerda != NULL) {
        atual = atual->esquerda;
    }

    return atual;
}

// Remover um no da arvore
struct No* remover(struct No* raiz, int valor) {
    if (raiz == NULL) {
        return raiz;
    }

    if (valor < raiz->valor) {
        raiz->esquerda = remover(raiz->esquerda, valor);  // Remover na subarvore esquerda
    } else if (valor > raiz->valor) {
        raiz->direita = remover(raiz->direita, valor);  // Remover na subarvore direita
    } else {
        // N� com apenas um filho ou nenhum
        if (raiz->esquerda == NULL) {
            struct No* temp = raiz->direita;
            free(raiz);
            return temp;
        } else if (raiz->direita == NULL) {
            struct No* temp = raiz->esquerda;
            free(raiz);
            return temp;
        }

        // N� com dois filhos: obt�m o sucessor (menor n� na subarvore direita)
        struct No* temp = menorValor(raiz->direita);
        raiz->valor = temp->valor;
        raiz->direita = remover(raiz->direita, temp->valor);  // Remove o sucessor
    }

    return raiz;
}

// Percurso em ordem (in-order traversal)
void emOrdem(struct No* raiz) {
    if (raiz != NULL) {
        emOrdem(raiz->esquerda);  // Visita a subarvore esquerda
        printf("%d ", raiz->valor);  // Visita a raiz
        emOrdem(raiz->direita);  // Visita a subarvore direita
    }
}

// Funcao principal
int main() {
    struct No* raiz = NULL;

    // Inserindo elementos na arvore
    raiz = inserir(raiz, 50);
    raiz = inserir(raiz, 30);
    raiz = inserir(raiz, 20);
    raiz = inserir(raiz, 40);
    raiz = inserir(raiz, 70);
    raiz = inserir(raiz, 60);
    raiz = inserir(raiz, 80);

    printf("Percurso em ordem da arvore: ");
    emOrdem(raiz);
    printf("\n");

    // Buscando um valor
    int valor = 40;
    struct No* resultado = buscar(raiz, valor);
    if (resultado != NULL) {
        printf("Valor %d encontrado na arvore.\n", valor);
    } else {
        printf("Valor %d nao encontrado na arvore.\n", valor);
    }

    // Removendo um valor
    raiz = remover(raiz, 20);
    printf("arvore apos remover 20: ");
    emOrdem(raiz);
    printf("\n");

    raiz = remover(raiz, 30);
    printf("arvore apos remover 30: ");
    emOrdem(raiz);
    printf("\n");

    raiz = remover(raiz, 50);
    printf("arvore apos remover 50: ");
    emOrdem(raiz);
    printf("\n");

    return 0;
}