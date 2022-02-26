from tkinter import *
from datetime import datetime
import locale

preto = "#3d3d3d"
branco = "#fafcff"

fundo = preto

janela = Tk()
janela.title("Relogio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=preto)

def relogio():
    tempo = datetime.now()

    locale.setlocale(locale.LC_TIME, "pt_BR")
    
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "," + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("Arial 80"), bg = fundo, fg = branco)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("Arial 20"), bg = fundo, fg = branco)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
