import auxiliar
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import os

class Grafo:

    def __init__(self):
        self.entradas = []
        self.e =[]
        self.maior_vertice = 0
        self.contador = 0
        self.colunas = len(self.entradas)

    def pega_vertices(self):
        vertices = [0, 0, 0]
        print("Digite os vertices: ")
        vertice_c_peso = list(map(int, input().split()))
        while (len(vertice_c_peso) != 0):
            if (auxiliar.verifica_repeticao(self.entradas,vertice_c_peso[0],vertice_c_peso[1])):
                self.e.append(vertice_c_peso)
                vertices = vertice_c_peso[0], vertice_c_peso[1], vertice_c_peso[2]
                self.entradas.append(vertices)
            print("Digite os vertices: ")
            vertice_c_peso = list(map(int, input().split()))

        print(self.entradas)
        print(self.e)

        for i in range(len(self.entradas)):
            for j in range(0, 2):
                if(self.entradas[i][j] > self.maior_vertice):
                    self.maior_vertice = self.entradas[i][j]

        self.escreve_adjacente()
        self.escreve_incidente()

    def adiciona_aresta(self,vertices_c_peso):
        vertices = [0,0,0]
        vertices= vertices_c_peso[0],vertices_c_peso[1],vertices_c_peso[2]
        if (auxiliar.verifica_repeticao(self.entradas,vertices_c_peso[0],vertices_c_peso[1])):
            self.entradas.append(vertices)
            self.e.append(vertices_c_peso)

        self.escreve_adjacente()
        self.escreve_incidente()
        self.desenhaGrafo()

    def remove_aresta(self,vertices):
        i = auxiliar.procura_aresta(self.entradas,vertices[0],vertices[1])
        del self.entradas[i]
        del self.e[i]
        self.escreve_adjacente()
        self.escreve_incidente()
        self.desenhaGrafo()

    def remove_no(self,no):
        aresta = auxiliar.procura_todas_arestas(self.entradas,no)
        for i in range (0,len(aresta)):
            self.remove_aresta(aresta[i])

        self.escreve_incidente()
        self.escreve_adjacente()
        self.desenhaGrafo()

    def printa_matriz(self):
        print('Matriz adjacente :\n')
        for i in range (0,len(self.matriz_adjacente)):
            print(self.matriz_adjacente[i])

        print('Matriz incidênte :\n')
        for i in range(0, len(self.matriz_incidente)):
            print(self.matriz_incidente[i])

    def modifica_aresta (self, entrada):
        i = auxiliar.procura_aresta(self.entradas,entrada[0],entrada[1])
        self.entradas[i][2] = entrada[2]
        self.e[i][2]= entrada[2]
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






    def desenhaGrafo(self, num):

        G = nx.Graph()
        plt.cla()
        plt.clf()
        E = self.entradas
        G.add_weighted_edges_from(E)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold")
        edge_weight = nx.get_edge_attributes(G,"weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.savefig('graph.png')



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

#
#     def menu(self):
#
#         self.pega_vertices()
#         self.desenhaGrafo()
#         self.printa_matriz()
#         n=1
#
#         while (n!=0):
#             print('\n')
#             print('Digite 1 para adicionar uma aresta :')
#             print('Digite 2 para remover uma aresta :')
#             print('Digite 3 para remover um nó :')
#             print('Digite 4 para modificar o comprimento de uma aresta :')
#             print('Digite 5 para modificar o peso de um vértice :\n')
#             n = int(input())
#
#             if (n == 1):
#                 print("Digite o vertice para adicionar: ")
#                 vertices_c_peso = list(map(int, input().split()))
#                 self.adiciona_aresta(vertices_c_peso)
#                 self.printa_matriz()
#             elif (n == 2):
#                 print('Digite a aresta que deseja remover:')
#                 aresta = list(map(int,input().split()))
#                 self.remove_aresta(aresta)
#                 self.printa_matriz()
#             elif (n == 3):
#                 print("Digite o nó para remover: ")
#                 no = int(input())
#                 self.remove_no(no)
#                 self.printa_matriz()
#             elif(n==4):
#                 print("Digite a aresta para modificar: ")
#                 aresta = list(map(int, input().split()))
#                 self.modifica_aresta(aresta[0],aresta[1],aresta[2])
#                 self.printa_matriz()
#             elif(n==5):
#                 print('Digite o vértice e seu novo peso :\n')
#                 v = list(map(int, input().split()))
#                 self.modifica_pesos(v[0],v[1])
#
#
#
#
#
# objeto = Grafo()
#
# #objeto.pega_vertices_com_pesos()
# objeto.menu()
# print("                         ")
#
#
#
#
#








