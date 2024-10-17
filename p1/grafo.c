#include <stdio.h>

#define MAX_VERTICES 5  // Define o número máximo de vértices

// Estrutura do Grafo
struct Grafo {
    int adj[MAX_VERTICES][MAX_VERTICES];  // Matriz de adjacência
    int numVertices;                      // Número de vértices
};

// Inicializa o Grafo
void inicializarGrafo(struct Grafo *g, int numVertices) {
    g->numVertices = numVertices;

    // Inicializa a matriz de adjacência com 0 (sem arestas)
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            g->adj[i][j] = 0;
        }
    }
}

// Adiciona uma aresta no grafo (não direcionado)
void adicionarAresta(struct Grafo *g, int v1, int v2) {
    if (v1 >= g->numVertices || v2 >= g->numVertices) {
        printf("Erro: Vértices inválidos.\n");
    } else {
        g->adj[v1][v2] += 1;  // Aresta de v1 para v2
        g->adj[v2][v1] += 1;  // Aresta de v2 para v1 (grafo não direcionado)
        printf("Aresta adicionada entre %d e %d.\n", v1, v2);
    }
}

// Exibe a matriz de adjacência
void exibirMatrizAdjacencia(struct Grafo *g) {
    printf("Matriz de Adjacência:\n");
    for (int i = 0; i < g->numVertices; i++) {
        for (int j = 0; j < g->numVertices; j++) {
            printf("%d ", g->adj[i][j]);
        }
        printf("\n");
    }
}

//Verifica se existe aresta
int existeAresta(struct Grafo g, int v1, int v2){
    return g.adj[v1][v2];
}

//Verifica caminho
int verificaCaminho(struct Grafo g, int caminho[], int tamanho_caminho){
    for(int i = 0; i < (tamanho_caminho-1); i++){
        if(!existeAresta(g,caminho[i], caminho[i+1]))
            return 0;
    }
    return 1;
}

// Função principal
int main() {
    struct Grafo g;
    inicializarGrafo(&g, MAX_VERTICES);

    adicionarAresta(&g, 0, 1);
    adicionarAresta(&g, 0, 2);
    adicionarAresta(&g, 1, 2);
    adicionarAresta(&g, 1, 3);
    adicionarAresta(&g, 3, 4);

    exibirMatrizAdjacencia(&g);

    printf("Aresta entre V2 e V3: %d\n", existeAresta(g,2,3));
    printf("Aresta entre V2 e V1: %d\n", existeAresta(g,2,1));

    int caminho1[3] = {0,1,3};
    int caminho2[5] = {0,4,3,1,0};

    printf("Caminho 1: %d\n", verificaCaminho(g,caminho1,3));
    printf("Caminho 2: %d\n", verificaCaminho(g,caminho2,5));

    return 0;
}