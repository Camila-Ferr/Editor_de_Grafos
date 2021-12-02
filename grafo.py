import adjacencia,incidencia
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:

    def __init__(self):
        self.entradas = []
        self.maior_vertice = 0
        self.pega_vertices()

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
        self.matriz_adjacente.adiciona(vertices[0],vertices[1],vertices[2])
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
        self.matriz_adjacente.remove_vertice(no)
        self.matriz_incidente.remove_vertice(no)
        #Achar o nó p remover



    def desenhaGrafo(self):
        G = nx.Graph()
        E = self.entradas
        G.add_weighted_edges_from(E)
        nx.draw(G, with_labels=True, font_weight="bold")
        plt.savefig("graph.png")






objeto = Grafo()
#objeto.pega_vertices_com_pesos()
objeto.desenhaGrafo()
print("                         ")













