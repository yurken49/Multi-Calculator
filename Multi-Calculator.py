#importmaos todas as bibliotecas que vamos usar
from tkinter import *
from math import *
from functools import partial as prt


#a nossa classe primcimpal
class Maquina(object):
	def __init__(self):
		#dfinimos como vai ser o nosso container
		self.janela = Tk()
		self.janela.title("Multi_calculator")
		self.janela.resizable(False, False)
		self.janela.geometry("400x600")
		self.janela["bg"] = "#17104b"

		#labela com a mensagem de boas vindas 
		self.lb1 = Label(self.janela, text = """WELCOME!
		CHOSSE AN OPTION PLEASE""", bg="#17104b", fg="white", font=('verdana', 12, 'italic'), pady=100, padx=20)
		self.lb1.pack()

		#criamos os radio buttons para o usuário escolher qual maquina quer usar
		self.rdbt1 = Checkbutton(self.janela, text="SCIENTIFIC CALCULATOR", bg="#17104b", fg="#5eff00", font=('verdana', 14, 'bold'))
		self.rdbt2 = Checkbutton(self.janela, text="STATISTIC CALCULATOR ", bg="#17104b", fg="#5eff00", font=('verdana', 14, 'bold'))
		self.rdbt3 = Checkbutton(self.janela, text="FINACIAL CONSULTANT  ", bg="#17104b", fg="#5eff00", font=('verdana', 14, 'bold'))

		#EMPACOTAMOS OS RADIO BUTTONS
		self.rdbt1.pack()
		self.rdbt2.pack()
		self.rdbt3.pack()





		#chamamos o nosso mainloop
		self.janela.mainloop()
#chamamos a nossa classe princimpal para rodar o projeto
Maquina()

