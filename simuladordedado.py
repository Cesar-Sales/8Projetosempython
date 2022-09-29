# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class Simuladordedado:
    def __init__(self):
        self.valorminimo = 1
        self.valormaximo = 6
        self.msg = "voce gostaria de gerar um novo valor para o dado?"
        #layout 
        self.layout = [ 
        [sg.Text('Jogar o dado?')],
        [sg.Button('sim'),sg.Button('nao')]
        ]
    
    def Iniciar(self):
        #janela
        self.janela = sg.Window('Simulador de dado',self.layout)

        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        if self.eventos == sg.WIN_CLOSED:
            sg.WINDOW_CLOSED
        #fazer algo com os valores
        
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValordoDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print("Ok.")
            else:
                print('favor ditar sim ou nao')
        except:
            print("Ocorreu um erro ao receber sua resposta, por favor responda em 'sim' ou 's'para SIM e 'nao ou 'n' para NAO")

    def GerarValordoDado(self):
        print(random.randint(self.valorminimo, self.valormaximo))

simulador = Simuladordedado()
simulador.Iniciar()



