import PySimpleGUI as sg


class Tela:

    def __init__(self):


        #Layout
        layout = [
            [sg.Text('Vértice 1:', size=(10,0)), sg.Input(size=(15,1)), sg.Text('Peso do Vértice 1:', size=(10,0)), sg.Input(size=(15,1))],
            [sg.Text('Vértice 2:', size=(10,0)), sg.Input(size=(15,1)), sg.Text('Peso do Vértice 2',size=(10,0)), sg.Input(size=(15,1))],
            [sg.Text('Comprimento da Aresta:', size=(10,0)), sg.Input(size=(15,1))],
            [sg.Button('Adicionar'), sg.Button('Remover Aresta'), sg.Button('Modificar Aresta') ]

        ]

        #janela

        window = sg.Window("Editor de Grafos", size=(1500,800)).layout(layout)

        #Extrair os dados da tela
        self.button, self.values = window.Read()

    def iniciar(self):
        print(self.values)



tela = Tela()
tela.iniciar()
