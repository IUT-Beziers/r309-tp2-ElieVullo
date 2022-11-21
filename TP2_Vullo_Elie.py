from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random

#Exercice 1 :


def move(position):
	global SwitchImage
	Objet1 = can1.create_image(position.x,position.y, image=SwitchImage)
	
def find_closest	

def affiche():
	
	B4 = Button(can, text='PC', height=2, width=12, bg='ivory', command = PC)
	B4.pack(side=LEFT)
	B5 = Button(can, text='Téléphone', height=2, width=12, bg='ivory', command = Telephone)
	B5.pack(side=LEFT)
	can.create_window(66, 400, window=B4)
	can.create_window(66, 450, window=B5)
		

def Switch():
	Image1 = can1.create_image(random.randint(0,300),random.randint(0,300), image = Images[0])
	can1.image = Images[0]

	
def Routeur():
	Image2 = can1.create_image(random.randint(0,300),random.randint(0,300), image = Images[1])
	can1.image = Images[1]
	
	
def PC():
	Image3 = can1.create_image(random.randint(0,300),random.randint(0,300), image = Images[2])
	can1.image = Images[2]
	
def Telephone():
	Image4 = can1.create_image(random.randint(0,300),random.randint(0,300), image = Images[3])
	can1.image = Images[3]
	

root = Tk()
root.title('Application réseau')
root.geometry('720x720')

SwitchImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/SwitchImage.png')
RouteurImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/RouteurImage.png')
PcImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/PcImage.png')
TelephoneImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/TelephoneImage.png')
Images = [SwitchImage, RouteurImage, PcImage, TelephoneImage]

font = font.Font(size=15, weight="bold")

can = Canvas(root, width=150, height=720, bg='ivory')
can.pack(side=LEFT)
can1 = Canvas(root, width=570, height=720, bg='white')
can1.pack(side=RIGHT)
can1.bind("<B1-Motion>", move)


Label1 = Label(can, text='Menu', width=300, height=7,borderwidth=2, bg='red')
Label1['font'] = font
Label1.pack()



B1 = Button(can, text='Switch', height=2, width=18, bg='gray', command = Switch)
B1.pack(side=LEFT)

B2 = Button(can, text='Client', height=2, width=18, bg='gray', command = affiche)
B2.pack(side=LEFT)

B3 = Button(can, text='Routeur', height=2, width=18, bg='gray', command = Routeur)
B3.pack(side=LEFT)

can.create_window(20, 60, window=Label1)
can.create_window(66, 200, window=B1)
can.create_window(66, 350, window=B2)
can.create_window(66, 500, window=B3)


root.mainloop()
