import PySimpleGUI as sg


class Tela:

    def __init__(self):
        sg.theme(new_theme='Reddit')
        sg.theme_border_width(border_width = 5)

        sg.theme_background_color(color = 'Pink')

        #Layout
        layout = [
            [sg.Text(' '*40, background_color='Pink'), sg.Text('Adicionar', size=(10,0), background_color='Pink', justification='left', font=('Arial, 11')),
             sg.Text(" "*50, background_color='Pink'), sg.Text('Remover \nAresta', size=(10,0), background_color='Pink', justification='left', font=('Arial, 11')),
             sg.Text(' '*30, background_color='Pink'), sg.Text('Modificar \nAresta', background_color='Pink', size=(10,0), justification='left', font=('Arial, 11')),
             sg.Text(' '*30, background_color='Pink'), sg.Text('Remover \nVértice', background_color='Pink', size=(10,0), justification='left', font=('Arial, 11')),
             sg.Text(' '*33, background_color='Pink'), sg.Text('Modificar \nVértice', background_color='Pink', size=(10,0), justification='left', font=('Arial, 11'))],

            [sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('vertice1', size=(10,1), key='vertice1'),
             sg.Text('Peso do Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('peso1', size=(10,1), key='peso1'),
             sg.Text(" "*5, background_color='Pink'), sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('v1_remove_aresta',size=(10,1), key='v1_remove_aresta'),
             sg.Text(" "*10, background_color='Pink'), sg.Text('Vértice 1', size=(10,0), background_color='Pink', justification='left'), sg.Input('v1_mod_aresta',size=(10,1), key='v1_mod_aresta'),
             sg.Text(' '*10, background_color='Pink'), sg.Text('Vértice \npara remoção:', size=(10,0), background_color='Pink', justification='left'), sg.Input('remove_v1', size=(10,1), key='remove_v1'),
             sg.Text(' '*10, background_color='Pink'), sg.Text('Vértice \npara modificação:', size=(12,0), background_color='Pink', justification='left'), sg.Input('modifica_v1', size=(10,1), key='modifica_v1')],


            [sg.Text('Vértice 2:', size=(10,0), background_color='Pink', justification='left'), sg.Input('vertice2', size=(10,1), key='vertice2'),
             sg.Text('Peso do Vértice 2:',size=(10,0), background_color='Pink', justification='left'), sg.Input('peso2',size=(10,1), key='peso2'),
             sg.Text(" "*5, background_color='Pink'), sg.Text('Vértice 2:', size=(10,0), background_color='Pink', justification='left'), sg.Input('v2_remove_aresta', size=(10,1), key='v2_remove_aresta'),
             sg.Text(' '*10, background_color='Pink'), sg.Text('Vértice 2:', size=(10,0), background_color='Pink', justification='left'), sg.Input('v2_mod_aresta', size=(10,1), key='v2_mod_aresta'),
             sg.Text(' '*78, background_color='Pink'), sg.Text('Novo Peso:', size=(10,0), background_color='Pink', justification='left'), sg.Input('novo_peso', size=(10,1), key='novo_peso')],


            [sg.Text('Comprimento da Aresta:', size=(10,0), background_color='Pink', justification='left'), sg.Input('comprimento', size=(10,1), key='comprimento'),
             sg.Text(' '*118, background_color='Pink'), sg.Text('Novo \nComprimento:', size=(10,0), background_color='Pink', justification='left'), sg.Input('novo_comprimento', size=(10,1), key='novo_comprimento')],

            [sg.Text(' '*30, background_color='Pink'), sg.Button('Adicionar', key='adicionar'), sg.Text(" "*55, background_color='Pink'),
             sg.Button('Remover Aresta',  key='remove_aresta'),
             sg.Text(' '*35, background_color='Pink'), sg.Button('Modificar Aresta', key='modifica_aresta'),
             sg.Text(' '*30, background_color='Pink'), sg.Button('Remove Vértice', key='remove_vertice'),
             sg.Text(' '*30, background_color='Pink'), sg.Button('Modificar Vértice', key='modifica_vertice')],

            [sg.Text('_'*208, background_color='Pink', justification='left')]

        ]


        #janela

        self.window = sg.Window("Editor de Grafos", size=(1500, 950)).layout(layout)



    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.window.Read()

            if (self.button == sg.WIN_CLOSED):
                break

            #if ##PROGRAMAR OS EVENTOS########





tela = Tela()
tela.iniciar()
