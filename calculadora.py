from tkinter import *
from tkinter import messagebox
from functools import partial


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


        # adicionando os componentes no frame
        # começando pela label que irá exibir os valores digitados pelo usuario
        # e seu respectivo resultado
        mostra_numeros = Label(janela, text='', bd=5, width=43, height=4)
        mostra_numeros.place(x=10, y=10)


        # Abaixo serão as funções para soma, subtrair, dividir, multiplicar
        # Função para somar dois valores
        def soma(valor1, valor2):
            """Soma valores"""

            try:
                resultado = float(valor1) + float(valor2)
                muda_valor_label(' = ' + str(resultado))
            except TypeError:
                messagebox.showinfo('Erro', 'Formato de numero invalido')


        # Função para subtrair dois valores
        def subtrair(valor1, valor2):
            """Subtrai valores"""

            try:
                resultado = float(valor1) - float(valor2)
                muda_valor_label(' = ' + str(resultado))
            except TypeError:
                messagebox.showinfo('Erro', 'Formato de numero invalido')


        # Função para multiplicar dois valores
        def multiplicar(valor1, valor2):
            """Multiplicar valores"""

            try:
                resultado = float(valor1) * float(valor2)
                muda_valor_label(' = ' + str(resultado))
            except TypeError:
                messagebox.showinfo('Erro', 'Formato de numero invalido')


        # Função para dividir dois valores
        def dividir(valor1, valor2):
            """Dividir valores"""

            try:
                resultado = float(valor1) / float(valor2)
                muda_valor_label(' = ' + str(resultado))
            except TypeError:
                messagebox.showinfo('Erro', 'Formato de numero invalido')
            except ZeroDivisionError:
                messagebox.showinfo('Erro', 'Divisão por zero')


        # função para alterar a label
        # mostrando os valores digitados pelo usuario
        def muda_valor_label(num: str):

            global display
            display = StringVar()

            """Função para mostrar os valores digitados"""
            counter = str(mostra_numeros['text'])
            valores_label = counter + num
            display = valores_label
            mostra_numeros.config(text=str(valores_label))


        # Função para pegar os dois valores numericos
        def pega_valores():

            global display

            for valor in display:
                if valor == '+':
                    display = display.split('+')
                    soma(float(display[0]), float(display[1]))
                elif valor == '-':
                    display = display.split('-')
                    subtrair(float(display[0]), float(display[1]))
                elif valor == '*':
                    display = display.split('*')
                    multiplicar(float(display[0]), float(display[1]))
                elif valor == '/':
                    display = display.split('/')
                    print(dividir(float(display[0]), float(display[1])))


        # função papra apagar texto da label
        def apagar_label():

            mostra_numeros.config(text=str(' '))

        # adicionando os botões numericos na ordem que aparecem em uma calculadora

        btn7 = Button(janela, text='7', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '7'))
        btn7.place(x=10, y=90)

        btn8 = Button(janela, text='8', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '8'))
        btn8.place(x=90, y=90)

        btn9 = Button(janela, text='9', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '9'))
        btn9.place(x=170, y=90)

        btn4 = Button(janela, text='4', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '4'))
        btn4.place(x=10, y=168)

        btn5 = Button(janela, text='5', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '5'))
        btn5.place(x=90, y=168)

        btn6 = Button(janela, text='6', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '6'))
        btn6.place(x=170, y=168)

        btn1 = Button(janela, text='1', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '1'))
        btn1.place(x=10, y=247)

        btn2 = Button(janela, text='2', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '2'))
        btn2.place(x=90, y=247)

        btn3 = Button(janela, text='3', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '3'))
        btn3.place(x=170, y=247)

        btn0 = Button(janela, text='0', bg='blue', fg='white', width=9, height=4,
                      command=partial(muda_valor_label, '0'))
        btn0.place(x=10, y=325)

        btn_ponto = Button(janela, text='.', bg='blue', fg='white', width=9, height=4,
                           command=partial(muda_valor_label, '.'))
        btn_ponto.place(x=90, y=325)

        btn_res = Button(janela, text='=', bg='blue', fg='white', width=9, height=4,
                         command=partial(pega_valores))
        btn_res.place(x=170, y=325)


        # botão para limpar o texto da label
        btn_limpa = Button(janela, text='C', bg='red', fg='white', width=9, height=3,
                           command=partial(apagar_label))
        btn_limpa.place(x=250, y=90)


        # adicionando os botões de operação
        # Adição, Subtração, Multiplicação e Divisão
        btn_div = Button(janela, text='/', bg='blue', fg='white', width=9, height=3,
                         command=partial(muda_valor_label, '/'))
        btn_div.place(x=250, y=151)

        btn_mult = Button(janela, text='*', bg='blue', fg='white', width=9, height=3,
                          command=partial(muda_valor_label, '*'))
        btn_mult.place(x=250, y=214)

        btn_sub = Button(janela, text='-', bg='blue', fg='white', width=9, height=3,
                         command=partial(muda_valor_label, '-'))
        btn_sub.place(x=250, y=277)

        btn_soma = Button(janela, text='+', bg='blue', fg='white', width=9, height=3,
                          command=partial(muda_valor_label, '+'))
        btn_soma.place(x=250, y=340)


        janela.mainloop()


if __name__ == '__main__':
    Calculadora()
