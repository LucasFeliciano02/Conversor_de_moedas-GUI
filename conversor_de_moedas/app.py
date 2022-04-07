# https://iconarchive.com/  =  baixar icones que vao do lado do nome do app == (xxx.ico)
# https://icons8.com/icons/set/password  =  Site para baixar icones que vao dentro do app  == (xxx.png)

# * OBS: MUDEI O FORMATO DAS MOEDAS PARA O PADRÃO BR  =  ex: 1.080,35 | 375,35

from tkinter import Tk, ttk
from tkinter import *

from PIL import ImageTk, Image  # Pillow
from tkinter import messagebox

import requests
import json
import string


# cores
cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#38576b"  # dark blue / azul escuro


# Configurando a janela
janela = Tk()
# janela.geometry('300x320')
janela.title('Conversor')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('Conversor.ico')  # icon do app


style = ttk.Style(janela)
style.theme_use('clam')


# ------- Divisao da janela com a criação de frames --------

frame_cima = Frame(janela, width=300, height=60, padx=0,
                   pady=0, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0, columnspa=2)

frame_baixo = Frame(janela, width=300, height=260, padx=0,
                    pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


# ------- Função Converter e Requisições --------

def converter():
    try:
        moeda_de = combo_de.get()
        moeda_para = combo_para.get()
        valor_entrado = float(valor.get())

        try:
            response = requests.get(
                'https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))

            cambio = response.json()['rates'][moeda_para]

            resultado = valor_entrado * float(cambio)

        except:
            messagebox.showerror(
                'Erro!', 'Verifique sua conexão com a internet e preencha todos os campos')
            return

        dict_moedas = {
            'USD': '$',
            'BRL': 'R$',
            'EUR': '€',
            'CAD': 'C$',
            'AUD': 'A$',
            'CHF': 'Fr',
            'JPY': '¥',
            'RUB': 'RUB',
            'INR': '₹',
            'AOA': 'Kz'
        }

        simbolo = dict_moedas[moeda_para]

        valor.delete(0, "end")

    except:
        messagebox.showinfo(
            'Atenção!', 'Preencha todos os campos com seus respectivos atributos\n')
        return

    # FORMATO BR
    moeda_equivalente = simbolo + '{:_.2f}'.format(resultado)
    app_resultado['text'] = moeda_equivalente.replace(
        '.', ',').replace('_', '.')

    # FORMATO EUA
    # moeda_equivalente = simbolo + '{:,.2f}'.format(resultado)
    # app_resultado['text'] = moeda_equivalente


# ------- Configuração para o frame_cima --------
icon = Image.open('Moeda.png')
icon = icon.resize((40, 40), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)

app_nome = Label(frame_cima, image=icon, compound=LEFT, text='Conversor de moeda ', height=5,
                 pady=30, padx=13, relief='raised', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)


# ------- Configuração para o frame_baixo --------

app_resultado = Label(frame_baixo, text='', width=16, height=2,
                      relief='solid', anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)


moeda = ['USD', 'BRL', 'EUR', 'CAD', 'AUD', 'CHF', 'JPY', 'RUB', 'INR', 'AOA']

# Combobox: De
app_de = Label(frame_baixo, text='De', width=8, height=1,
               relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_de.place(x=48, y=90)

combo_de = ttk.Combobox(frame_baixo, width=8,
                        justify=CENTER, font=('Ivy 12 bold'))
combo_de.place(x=50, y=115)
combo_de['values'] = (moeda)


# Combobox: Para
app_para = Label(frame_baixo, text='Para', width=8, height=1,
                 relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_para.place(x=158, y=90)

combo_para = ttk.Combobox(frame_baixo, width=8,
                          justify=CENTER, font=('Ivy 12 bold'))
combo_para.place(x=160, y=115)
combo_para['values'] = (moeda)


# ------- entry (vai de baixo do De e Para) --------

valor = Entry(frame_baixo, width=22, justify=CENTER,
              font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=160)


# ------- Botao --------

botao = Button(frame_baixo, command=converter, text='Converter ', width=19, padx=5,
               height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=50, y=210)


# * Centralizando o arquivo

# Dimensoes da janela
largura = 300
altura = 320

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
