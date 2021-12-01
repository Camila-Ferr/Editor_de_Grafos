import adjacencia,incidencia

class Grafo:

    def __init__(self):
        self.matriz_adjacente = []
        self.matriz_incidente = []
        self.entradas = []
        self.maior_vertice = 0


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

    #def pega_vertices_arestas(self):
     #   conjunto = []
      #  entrada = [0,0,0]
       # linhas = 0
        #arestas_vertices =[]

        #Recebe as arestas e os vértices
        #while (len(entrada) == 3):
         #   entrada = list(input("Digite o inicio e o final do vértice, e a aresta: \n").split())
          #  arestas_vertices.append(entrada)

        #del arestas_vertices[-1]
        #linhas = len(arestas_vertices)

        #Verifica se todos os vértices são inteiros e pega o maior vértice
        #colunas = -1
        #for a in range (0,len(arestas_vertices)):
         #   for b in range (0,2):
          #      try:
           #         arestas_vertices[a][b]= int(arestas_vertices[a][b])
            #        if (arestas_vertices[a][b]>colunas):
             #           colunas = arestas_vertices[a][b]
              #  except:
               #     print("Um erro foi detectado na entrada.")
                #    break

        #self.matriz_incidente = incidencia.Incidente(arestas_vertices, linhas,colunas)







objeto = Grafo()
#objeto.pega_vertices_com_pesos()
objeto.pega_vertices()

print("                         ")













