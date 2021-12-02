class Incidente:

    def __init__(self, vertices_arestas, colunas,linhas):

        self.vertices_arestas = vertices_arestas
        self.colunas = colunas
        self.linhas = linhas
        self.matriz_incidente =[]
        self.escreve_incidente()

    def escreve_incidente(self):
        matriz =[]

        # Cria matriz zerada
        for i in range (0, self.linhas):
            linha = [0]*self.colunas
            matriz.append(linha)

        for lin in range (0, len(self.vertices_arestas)):
            for col in range (0,2):
                indice = self.vertices_arestas[lin][col]
                matriz[indice-1][lin] = 1

        self.matriz_incidente = matriz

    def adiciona(self,verti1, verti2,peso):

        entrada =[verti1,verti2,peso]
        diferenca = 0
        self.vertices_arestas.append(entrada)

        if ((verti1 > self.linhas) or (verti2 > self.linhas)):
            diferenca1 = verti1 - self.linhas
            diferenca2 = verti2 - self.linhas

            if (diferenca1 >= diferenca2):
                diferenca = diferenca1
            else:
                diferenca = diferenca2
        print(self.colunas)
        self.colunas += 1
        print(self.colunas)
        print(self.linhas)
        self.linhas += diferenca
        print(self.linhas)
        self.escreve_incidente()

    def procura_todas_arestas(self,verti1):
        arestas =[]

        for i in range (0,len(self.vertices_arestas)):
            for j in range (0,2):

                if self.vertices_arestas[i][j] == verti1:
                    arestas.append(self.vertices_arestas[i])
        return arestas

    def procura_aresta (self,verti1,verti2):
        linha = -1
        for i in range (0,len(self.vertices_arestas)):
            if (((self.vertices_arestas[i][0] == verti1) and (self.vertices_arestas[i][1] == verti2)) or
                        ((self.vertices_arestas[i][0] == verti2) and (self.vertices_arestas[i][1] == verti1))):
                linha = i
                break
        return linha

    def remove_aresta(self,verti1,verti2):

        i = self.procura_aresta(verti1,verti2)

        del self.vertices_arestas[i]
        self.colunas -=1

        self.escreve_incidente()


    def remove_vertice (self,verti1):
        arestas = self.procura_todas_arestas(verti1)

        for i in range (0,len(arestas)):
            self.remove_aresta(arestas[i][0],arestas[i][1])

        del self.matriz_incidente[verti1-1]

