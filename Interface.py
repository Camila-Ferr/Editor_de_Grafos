import PySimpleGUI as sg


class Tela:

    def __init__(self):
        sg.theme(new_theme='Reddit')
        sg.theme_border_width(border_width = 5)

        sg.theme_background_color(color = 'Pink')

        #Layout
        layout = [
            [sg.Text('Adicionar', size=(10,0), background_color='Pink', justification='left'), sg.Text(" "*90, background_color='Pink'), sg.Text('Remover Aresta')],
            [sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='vertice1'), sg.Text('Peso do Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='peso1'),
             sg.Text(" "*5, background_color='Pink'), sg.Text('Vértice 1:', size=(0,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='vertice1_mod')],

            [sg.Text('Vértice 2:', size=(10,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='vertice1'), sg.Text('Peso do Vértice 2:',size=(10,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='peso2')],
            [sg.Text('Comprimento da Aresta:', size=(10,0), background_color='Pink', justification='left'), sg.Input(size=(10,1), key='comprimento')],
            [sg.Button('Adicionar', key='adicionar'), sg.Button('Remover Aresta',  key='remove_aresta'), sg.Button('Modificar Aresta', key='modifica_aresta') ]

        ]


        #janela

        self.window = sg.Window("Editor de Grafos", size=(1500, 950)).layout(layout)



    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.window.Read()

            if self.button == sg.WIN_CLOSED:
                break

            #if ##PROGRAMAR OS EVENTOS########





tela = Tela()
tela.iniciar()
