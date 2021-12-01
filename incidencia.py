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
        print(self.matriz_incidente)

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

        self.colunas += 1
        self.linhas += diferenca
        self.escreve_incidente()

    def remove_aresta (self,verti1,verti2):

        for i in range (0,len(self.vertices_arestas)):

            if (((self.vertices_arestas[i][0] == verti1) and (self.vertices_arestas[i][1] == verti2)) or
                    ((self.vertices_arestas[i][1] == verti2) and (self.vertices_arestas[i][1] == verti1))):

                del self.vertices_arestas[i]
                self.colunas -=1

                if (verti1 == self.linhas) or (verti2 == self.linhas):
                    self.linhas -=1

                self.escreve_incidente()
                break
                
