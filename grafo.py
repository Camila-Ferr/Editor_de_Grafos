import adjacencia,incidencia
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import os

class Grafo:

    def __init__(self):
        self.entradas = []
        self.maior_vertice = 0
        self.contador = 0

    def pega_vertices(self):
        vertices = [0, 0, 0]
        print("Digite os vertices: ")
        vertices = list(map(int, input().split()))
        while (len(vertices) != 0):
            self.entradas.append(vertices)
            print("Digite os vertices: ")
            vertices = list(map(int, input().split()))


        print(self.entradas)

        for i in range(len(self.entradas)):
            for j in range(0, 2):
                if(self.entradas[i][j] > self.maior_vertice):
                    self.maior_vertice = self.entradas[i][j]

        self.matriz_adjacente = adjacencia.Adjacente(self.entradas, self.maior_vertice)
        self.matriz_incidente = incidencia.Incidente(self.entradas, len(self.entradas),self.maior_vertice)

    def adiciona_aresta(self):
        print("Digite o vertice para adicionar: ")
        vertices = list(map(int, input().split()))
        #self.matriz_adjacente.adiciona(vertices[0],vertices[1],vertices[2])
        self.matriz_incidente.adiciona(vertices[0],vertices[1],vertices[2])
        self.entradas.append(vertices)
        self.desenhaGrafo()

    def remove_aresta(self):
        print("Digite o vertice para remover: ")
        vertices = list(map(int, input().split()))
        self.matriz_adjacente.remove_aresta(vertices[0], vertices[1])
        self.matriz_incidente.remove_aresta(vertices[0], vertices[1])

        #Achar o vértice p remover
        self.desenhaGrafo()

    def remove_no(self):
        print("Digite o nó para remover: ")
        no= int(input())
        #self.matriz_adjacente.remove_vertice(no)
        self.matriz_incidente.remove_vertice(no)
        #Achar o nó p remover
        self.desenhaGrafo()

    def printa_matriz(self):
        print('Matriz adjacente :\n')
        for i in range (0,len(self.matriz_adjacente.matriz_adjacente)):
            print(self.matriz_adjacente.matriz_adjacente[i])

        print('Matriz incidênte :\n')
        for i in range(0, len(self.matriz_incidente.matriz_incidente)):
            print(self.matriz_incidente.matriz_incidente[i])

    def desenhaGrafo(self):
        G = nx.Graph()
        plt.cla()
        plt.clf()
        E = self.entradas
        G.add_weighted_edges_from(E)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold")
        edge_weight = nx.get_edge_attributes(G,"weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.show()


    def menu(self):

        self.pega_vertices()
        self.desenhaGrafo()
        self.printa_matriz()
        n=1

        while (n!=0):
            print('\n')
            print('Digite 1 para adicionar uma aresta :')
            print('Digite 2 para remover uma aresta :')
            print('Digite 3 para remover um nó :\n')
            n = int(input())

            if (n == 1):
                self.adiciona_aresta()
                self.printa_matriz()
            elif (n == 2):
                self.remove_aresta()
                self.printa_matriz()
            elif (n == 3):
                self.remove_no()
                self.printa_matriz()





objeto = Grafo()
#objeto.pega_vertices_com_pesos()
objeto.menu()
print("                         ")













