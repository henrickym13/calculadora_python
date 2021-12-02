from tkinter import *
from tkinter import messagebox
from functools import partial
from time import sleep


class Calculadora(Frame):
    """Janela Principal"""

    def __init__(self):
        """Método Construtor da janela"""

        # Definindo o titulo, largura, altura e cor de fundo da janela
        janela = Tk()
        janela.title('Calculadora')
        janela.maxsize(333, 405)
        janela.minsize(333, 405)
        janela.config(bg='black')

        # centralizar o frame na tela
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (333/2))
        y_cordinate = int((screen_height/2) - (405/2))
        janela.geometry("{}x{}+{}+{}".format(333, 405, x_cordinate, y_cordinate))

        # adicionando os componentes no frame
        # começando pela label que irá exibir os valores digitados pelo usuario
        # e seu respectivo resultado
        self.mostra_numeros = Label(janela, text='', bd=5, background='gray',
         font='arial 24', fg='white')
        self.mostra_numeros.place(x=10, y=10, width=312, height=70)

        # adicionando os botões numericos na ordem que aparecem em uma calculadora
        # primeira fileira de botões numericos
        btn7 = Button(janela, text='7', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '7'))
        btn7.place(x=10, y=90, width=73, height=70)
        btn8 = Button(janela, text='8', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '8'))
        btn8.place(x=90, y=90, width=73, height=70)
        btn9 = Button(janela, text='9', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '9'))
        btn9.place(x=170, y=90, width=73, height=70)

        # segunda fileira de botões numericos
        btn4 = Button(janela, text='4', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '4'))
        btn4.place(x=10, y=168, width=73, height=70)
        btn5 = Button(janela, text='5', bg='blue', fg='white', font='arial 14', 
            command=partial(self.muda_valor_label, '5'))
        btn5.place(x=90, y=168, width=73, height=70)
        btn6 = Button(janela, text='6', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '6'))
        btn6.place(x=170, y=168, width=73, height=70)

        # terceira fileira de botões numericos
        btn1 = Button(janela, text='1', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '1'))
        btn1.place(x=10, y=247, width=73, height=70)
        btn2 = Button(janela, text='2', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '2'))
        btn2.place(x=90, y=247, width=73, height=70)
        btn3 = Button(janela, text='3', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '3'))
        btn3.place(x=170, y=247, width=73, height=70)

        # quarta fileira de botões numericos
        btn0 = Button(janela, text='0', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '0'))
        btn0.place(x=10, y=325, width=73, height=71)
        btn_ponto = Button(janela, text='.', bg='blue', fg='white', font='arial 14',
            command=partial(self.muda_valor_label, '.'))
        btn_ponto.place(x=90, y=325, width=73, height=71)
        btn_resultado = Button(janela, text='=', bg='blue', fg='white', 
            font='arial 14', command=partial(self.pega_valores))
        btn_resultado.place(x=170, y=325, width=73, height=71)

        # botão para limpar o texto da label
        btn_limpa = Button(janela, text='C', bg='red', fg='white', font='arial 14',
            command=partial(self.apagar_label))
        btn_limpa.place(x=250, y=90, width=73, height=55)

        # adicionando os botões de operação
        # Adição, Subtração, Multiplicação e Divisão
        btn_divisao = Button(janela, text='/', bg='blue', fg='white',
            font='arial 14', command=partial(self.muda_valor_label, '/'))
        btn_divisao.place(x=250, y=151, width=73, height=55)

        btn_multiplicacao = Button(janela, text='*', bg='blue', fg='white',
            font='arial 14', command=partial(self.muda_valor_label, '*'))
        btn_multiplicacao.place(x=250, y=214, width=73, height=55)

        btn_subtrair = Button(janela, text='-', bg='blue', fg='white',
        font='arial 14', command=partial(self.muda_valor_label, '-'))
        btn_subtrair.place(x=250, y=277, width=73, height=55)

        btn_soma = Button(janela, text='+', bg='blue', fg='white',
        font='arial 14', command=partial(self.muda_valor_label, '+'))
        btn_soma.place(x=250, y=340, width=73, height=55)

        # manter a janela em loop
        janela.mainloop()
    

    def soma(self, valor1, valor2):
        """Método para realizar a soma dos valores"""

        resultado = float(valor1) + float(valor2)
        self.mostra_numeros.config(text=resultado)
    

    def subtrair(self, valor1, valor2):
        """Método para realizar a subtração dos valores"""
        resultado = float(valor1) - float(valor2)
        self.mostra_numeros.config(text=resultado)
    

    def multiplicar(self, valor1, valor2):
        """Método para realizar multiplicar os valores"""
        resultado = float(valor1) * float(valor2)
        self.mostra_numeros.config(text=resultado)
    

    def dividir(self, valor1, valor2):
        """Método para dividir os valores"""

        try:
            resultado = float(valor1) / float(valor2)
            self.mostra_numeros.config(text=round(resultado, 2))

        except ZeroDivisionError:
            messagebox.showerror('Erro', 'Divisão por zero!')

 
    def muda_valor_label(self, num: str):
        # mostrando os valores digitados pelo usuario

        # variavel global que vai armazenar todos os valores digitados
        global display
        display = StringVar()

        """Função para mostrar os valores digitados"""
        counter = str(self.mostra_numeros['text'])
        valores_label = counter + num
        display = valores_label
        self.mostra_numeros.config(text=str(valores_label))


    def pega_valores(self):
        # Função para pegar os  valores digitados

        # variavel global
        global display

        # executando for para saber qual operação foi selecionada e
        # chamar o método
        for valor in display:
            if valor == '+':
                display = display.split('+')
                self.soma(display[0], display[1])
            elif valor == '-':
                display = display.split('-')
                self.subtrair(display[0], display[1])
            elif valor == '*':
                display = display.split('*')
                self.multiplicar(display[0], display[1])
            elif valor == '/':
                display = display.split('/')
                self.dividir(display[0], display[1])

        
    def apagar_label(self):
        # função papra apagar texto da label

        self.mostra_numeros.config(text=str(' '))


if __name__ == '__main__':
    Calculadora()
