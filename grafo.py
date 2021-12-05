import auxiliar
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import os

class Grafo:

    def __init__(self):
        self.entradas = []
        self.e =[]
        self.v = []
        self.maior_vertice = 0
        self.contador = 0
        self.colunas = len(self.entradas)

    def adiciona_aresta(self,vertices_c_peso):
        vertices= vertices_c_peso[0],vertices_c_peso[1],vertices_c_peso[2]
        if (auxiliar.verifica_repeticao(self.entradas,vertices_c_peso[0],vertices_c_peso[1])):
            self.entradas.append(vertices)
            self.e.append(vertices_c_peso)

        self.escreve_adjacente()
        self.escreve_incidente()
        self.desenhaGrafo()

    def remove_aresta(self,vertices):
        i = auxiliar.procura_aresta(self.entradas,vertices[0],vertices[1])

        peso1 = self.e[i][3]
        peso2 = self.e[i][4]
        del self.entradas[i]
        del self.e[i]
        if(auxiliar.atualiza_no(self.entradas,vertices[0])):
            self.v.append([vertices[0],peso1])
        if (auxiliar.atualiza_no(self.entradas,vertices[1]) and auxiliar.verifica_repeticao(self.v,vertices[0],vertices[1])):
            self.v.append([vertices[1],peso2])

        self.escreve_adjacente()
        self.escreve_incidente()
        self.desenhaGrafo()

    def remove_no(self,no):
        aresta = auxiliar.procura_todas_arestas(self.entradas,no)

        for i in range (0,len(aresta)):
            self.remove_aresta(aresta[i])

        for i in range (0,len(self.v)):
            if (self.v[i][0] == no):
                del self.v[i]
                break

        self.escreve_incidente()
        self.escreve_adjacente()
        self.desenhaGrafo()

    def modifica_aresta (self, entrada):
        i = auxiliar.procura_aresta(self.entradas,entrada[0],entrada[1])
        self.entradas[i][2] = entrada[2]
        self.e[i][2] = entrada[2]
        self.escreve_incidente()
        self.escreve_adjacente()
        self.desenhaGrafo()

    def modifica_pesos (self, vert1, peso):
        aux = auxiliar.procura_todas_arestas(self.entradas,vert1)
        for i in range (0, len(aux)):
            indice = auxiliar.procura_aresta(self.e,aux[i][0],aux[i][1])
            if (self.e[indice][0] == vert1):
                self.e[indice][3] = peso
            else:
                self.e[indice][4] = peso


    def desenha_matriz_adjacente (self):
        fig, ax = plt.subplots(1, 1)
        column_labels = []

        for j in range (0,(auxiliar.atualiza_maior(self.entradas,-1))):
            column_labels.append(j+1)
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.matriz_adjacente, colLabels=column_labels, loc="center", rowLabels=column_labels)
        plt.show()

    def desenha_matriz_incidente(self):
        fig, ax = plt.subplots(1, 1)
        colunas = []
        linha = []
        for j in range(0, (auxiliar.atualiza_maior(self.entradas, -1))):
            colunas.append(j + 1)
        for i in range (0, len(self.entradas )):
            linha.append(chr(i+65))

        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.matriz_incidente, colLabels=linha ,loc="center", rowLabels=colunas)
        plt.show()

    def limpa_grafo(self):
        self.entradas = []
        self.e = []
        self.v = []
        self.maior_vertice = 0
        self.contador = 0
        self.colunas = len(self.entradas)

        self.desenhaGrafo()

    def desenhaGrafo(self):

        G = nx.Graph()
        plt.cla()
        plt.clf()
        E = self.entradas
        for i in range(0, len(self.v)):
            G.add_node(self.v[i][0])
        G.add_weighted_edges_from(E)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold")
        edge_weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.savefig('graph.png')
        plt.close()

    def desenhaGrafoSeparado(self):

        G = nx.Graph()
        plt.cla()
        plt.clf()
        E = self.entradas
        for i in range(0, len(self.v)):
            G.add_node(self.v[i][0])
        G.add_weighted_edges_from(E)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold")
        edge_weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.show()

    def tabela_pesos(self):
        pesos = []
        vertices = []
        for i in range(0, len(self.e)):
            vertice1 = self.e[i][0]
            vertice2 = self.e[i][1]
            peso1 = self.e[i][3]
            peso2 = self.e[i][4]

            if vertice1 not in vertices:
                pesos.append([vertice1, peso1])
                vertices.append(vertice1)

            if vertice2 not in vertices:
                pesos.append([vertice2, peso2])
                vertices.append(vertice2)

        for j in range(0, len(self.v)):
            pesos.append([self.v[j][0], self.v[j][1]])

        fig, ax = plt.subplots(1, 1)
        column_labels = ["Vértice", "Peso"]
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=pesos, colLabels=column_labels, loc="center")
        ax.set_facecolor('Blue')

        plt.show()

    def escreve_incidente(self):

        self.colunas = len(self.entradas)
        self.maior_vertice = auxiliar.atualiza_maior(self.entradas,-1)
        matriz =[]

        # Cria matriz zerada
        for i in range (0, self.maior_vertice):
            linha = [0]*self.colunas
            matriz.append(linha)

        for lin in range (0, len(self.entradas)):
            for col in range (0,2):
                indice = self.entradas[lin][col]
                matriz[indice-1][lin] = 1

        self.matriz_incidente = matriz

    def escreve_adjacente(self):

        self.maior_vertice = auxiliar.atualiza_maior(self.entradas, -1)
        self.colunas = len(self.entradas)
        self.matriz_adjacente = []
        for i in range(self.maior_vertice):
            lista = [0] * self.maior_vertice
            self.matriz_adjacente.append(lista)

        for i in range(len(self.entradas)):
            self.matriz_adjacente[self.entradas[i][0] - 1][self.entradas[i][1] - 1] = self.entradas[i][2]
            self.matriz_adjacente[self.entradas[i][1] - 1][self.entradas[i][0] - 1] = self.entradas[i][2]
