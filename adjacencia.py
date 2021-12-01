class Adjacente:

    def __init__(self, entradas, maior_vertice):

        self.entradas = entradas
        self.maior_vertice = maior_vertice
        self.matriz_adjacente = []
        self.cria_adjacente()

    def cria_adjacente(self):
        for i in range(self.maior_vertice):
            lista = [0] * self.maior_vertice
            self.matriz_adjacente.append(lista)

        for i in range(len(self.entradas)):
            print(i)
            self.matriz_adjacente[self.entradas[i][0] - 1][self.entradas[i][1] - 1] = self.entradas[i][2]
            self.matriz_adjacente[self.entradas[i][1] - 1][self.entradas[i][0] - 1] = self.entradas[i][2]

        print(self.matriz_adjacente)
