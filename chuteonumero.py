### decida por mim
import PySimpleGUI as sg
import random

class Decidapormim:
       
    def Iniciar(self):
        
        self.resposta = [ 
            
        
            'Deveria.',
            'Acho que nao hein.',
            'Faz isso nao, vai se arrepender',
            'Faz isso pra caralho pprt',
            'Sim.',
            'Não.',
            'SIM',
            'Nao deveria.'
            
        
            ]
        
        layout = [ 
            [sg.Text('---------- Pergunte se voce deve fazer o que realmente está em duvida e receba uma resposta do computador :) ',size=(20,10))],
            [sg.Input()],
            [sg.Button('Decida por mim')],
            [sg.Output(size=(30,10))],
            [sg.Button('Sair')]
        ]    
       #criar a janela
        self.janela = sg.Window('Decida por mim', layout) 
        while True:
       
       #ler os valores da janela
            self.elemento = random.choice(self.resposta)
            self.evento, self.valores = self.janela.Read()
        #fazer algo com os valores
            if self.evento == sg.WIN_CLOSED or self.evento == 'Sair': # if user closes window or clicks cancel
                break
            
            elif self.evento == 'Decida por mim':
                print(self.elemento)
            
            
decida = Decidapormim()
decida.Iniciar()            
janela.close()      
                
        