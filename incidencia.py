class Incidente:

    def __init__(self, vertices_arestas, linhas,colunas):

        self.vertices_arestas = vertices_arestas
        self.colunas = colunas
        self.linhas = linhas
        self.matriz_incidente =[]
        self.cria_incidente()

    def cria_incidente(self):
        matriz =[]

        # Cria matriz zerada
        for i in range (0, self.colunas):
            linha = [0]*self.linhas
            matriz.append(linha)

        for lin in range (0, len(self.vertices_arestas)):
            for col in range (0,2):
                indice = self.vertices_arestas[lin][col]
                matriz[indice-1][lin] = 1

        self.matriz_incidente = matriz
        print(self.matriz_incidente)

