class Adjacente:

    def __init__(self, entradas, maior_vertice):

        self.entradas = entradas
        self.maior_vertice = maior_vertice
        self.matriz_adjacente = []
        self.escreve_adjacente()

    def escreve_adjacente(self):
        self.matriz_adjacente = []
        for i in range(self.maior_vertice):
            lista = [0] * self.maior_vertice
            self.matriz_adjacente.append(lista)

        for i in range(len(self.entradas)):
            self.matriz_adjacente[self.entradas[i][0] - 1][self.entradas[i][1] - 1] = self.entradas[i][2]
            self.matriz_adjacente[self.entradas[i][1] - 1][self.entradas[i][0] - 1] = self.entradas[i][2]


    def adiciona(self, vert1, vert2, peso_arest):

        novos_vertices = [vert1, vert2, peso_arest]
        self.entradas.append(novos_vertices)
        self.atualiza_maior()
        self.escreve_adjacente()


    def remove_aresta(self, vert1, vert2):

        for i in range(len(self.entradas)):
            if(self.entradas[i][0]==vert1 and self.entradas[i][1]==vert2):
                self.entradas.pop(i)
                self.atualiza_maior()
                self.escreve_adjacente()



    def remove_vertice(self, vertice):

        for i in range(len(self.entradas)):
            if(self.entradas[i][0]==vertice or self.entradas[i][1]):
                self.entradas.pop(i)
                self.escreve_adjacente()


    def atualiza_maior(self):

        for i in range(len(self.entradas)):
            if(self.entradas[i][0] > self.maior_vertice):
                self.maior_vertice = self.entradas[i][0]

            elif(self.entradas[i][1] > self.maior_vertice):
                self.maior_vertice = self.entradas[i][1]

