import networkx as nx
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import io
from grafo import Grafo

GRAFO = Grafo()

sg.theme(new_theme='Reddit')
sg.theme_border_width(border_width = 5)

sg.theme_background_color(color = 'Pink')

#Layout
layout = [
    [sg.Text(' '*33, background_color='Pink'), sg.Text('Adicionar', size=(15,0), background_color='Black', justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text(" "*30, background_color='Pink'), sg.Text('Remover Aresta', size=(15,0), background_color='Black', justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text(' '*20, background_color='Pink'), sg.Text('Modificar Aresta', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text(' '*20, background_color='Pink'), sg.Text('Remover Vértice', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text(' '*23, background_color='Pink'), sg.Text('Modificar Vértice', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White')],

    [sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('vertice1', size=(10,1), key='vertice1'),
     sg.Text('Peso do Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('peso1', size=(10,1), key='peso1'),
     sg.Text(" "*5, background_color='Pink'), sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('v1_remove_aresta',size=(10,1), key='v1_remove_aresta'),
     sg.Text(" "*10, background_color='Pink'), sg.Text('Vértice 1:', size=(10,0), background_color='Pink', justification='left'), sg.Input('v1_mod_aresta',size=(10,1), key='v1_mod_aresta'),
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

    [sg.Text('_'*208, background_color='Pink', justification='left')],

    [sg.Text(' '*330, background_color='Pink'), sg.Button("Visualizar Graph", key='visualisar_grafo')],

    [sg.Image(key='-IMAGEM-')],





]

    #janela

window = sg.Window("Editor de Grafos",layout, finalize=True, size=(1500, 950))

def atualiza_frame():
    image = Image.open("graph.png")
    image.thumbnail((900, 900))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGEM-"].update(data=bio.getvalue())





while True:
    # Extrair os dados da tela
    event, values = window.Read()


    if (event == sg.WIN_CLOSED):
        break

    elif (event == 'adicionar'):

        entrada = [0]*5
        entrada[0] = int(values['vertice1'])
        entrada[1] = int(values['vertice2'])
        entrada[2] = int(values['comprimento'])
        entrada[3] = int(values['peso1'])
        entrada[4] = int(values['peso2'])
        GRAFO.adiciona_aresta(entrada)
        atualiza_frame()

    elif (event == 'remove_aresta'):

        entrada = [0] * 2
        entrada[0] = int(values['v1_remove_aresta'])
        entrada[1] = int(values['v2_remove_aresta'])
        GRAFO.remove_aresta(entrada)
        atualiza_frame()

    elif (event == 'modifica_aresta'):

        entrada = [0] * 3
        entrada[0] = int(values['v1_mod_aresta'])
        entrada[1] = int(values['v2_mod_aresta'])
        entrada[2] = int(values['novo_comprimento'])
        GRAFO.modifica_aresta(entrada)
        atualiza_frame()

    elif (event == 'remove_vertice'):
        entrada = [0]
        entrada[0] = values['remove_v1']
        GRAFO.remove_no(entrada[0])
        atualiza_frame()

    elif (event == 'modifica_vertice'):
        entrada = [0]*2
        entrada[0] = values['modifica_v1']
        entrada[1] = values['novo_peso']
        GRAFO.modifica_pesos(entrada[0], entrada[1])
        atualiza_frame()
        print(GRAFO.entradas[0][2])

    elif (event == 'visualisar_grafo'):

        GRAFO.desenhaGrafo(1)









