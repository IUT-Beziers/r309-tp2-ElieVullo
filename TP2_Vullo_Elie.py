from tkinter import *
from tkinter import ttk

#Exercice 1 : 

def affiche():
	
	B4 = Button(can, text='PC', height=2, width=12, bg='ivory', command = PC)
	B4.pack(side=LEFT)
	B5 = Button(can, text='Téléphone', height=2, width=12, bg='ivory', command = Telephone)
	B5.pack(side=LEFT)
	can.create_window(66, 400, window=B4)
	can.create_window(66, 450, window=B5)

def Switch():
	SwitchImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/SwitchImage.png')
	Objet = can1.create_image(300, 300, image = SwitchImage)
	can1.image = SwitchImage
	
def Routeur():
	RouteurImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/RouteurImage.png')
	Objet1 = can1.create_image(300, 300, image = RouteurImage)
	can1.image = RouteurImage
	
def PC():
	PcImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/PcImage.png')
	Objet2 = can1.create_image(300, 300, image = PcImage)
	can1.image = PcImage
	
def Telephone():
	TelephoneImage = PhotoImage(file='/home/e/elie.vullo/Téléchargements/TelephoneImage.png')
	Objet3 = can1.create_image(300, 300, image = TelephoneImage)
	can1.image = TelephoneImage
	
	
	
root = Tk()
root.title('Application réseau')
root.geometry('720x720')

can = Canvas(root, width=150, height=720, bg='ivory')
can.pack(side=LEFT)
can1 = Canvas(root, width=570, height=720, bg='white')
can1.pack(side=RIGHT)
can1.bind('<S>', Switch)
can1.bind('<s>', Switch)
can1.bind('<R>', Routeur)
can1.bind('<r>', Routeur)

Label1 = Label(can, text='Menu', width=150, height=7, bg='red')
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
