from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random

#Exercice 1 :

def Cable(e):
	x = e.x
	y = e.y
	if can1.old_coords:
		x1, y1 = can1.old_coords
		can1.create_line(x, y, x1, y1, width=5)
	can1.old_coords = x,y

def move(a):
	bn = 1
	x = a.x
	y = a.y
	item = can1.find_closest(a.x, a.y)
	while bn < 1 :
		item(a.x, a.y) == item(x,y)

def affiche():
	
	B4 = Button(can, text='PC                    ', width=170, bg='ivory', command = PC, image = ImagesBouton[2], compound=RIGHT)
	B4.pack(side=LEFT)
	B5 = Button(can, text='Téléphone           ', width=170, bg='ivory', command = Telephone, image = ImagesBouton[3], compound=RIGHT)
	B5.pack(side=LEFT)
	can.create_window(66, 400, window=B4)
	can.create_window(66, 450, window=B5)

def Tsuppr():
	j = 0
	while j < 1 :
		can1.delete(root, can1.find_closest(300, 300)[0] )
		
def suppr(position):
	x = position.x
	y = position.y
	item = can1.find_closest(position.x, position.y)[0]
	can1.delete(root,item)

def Switch():
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image1 = can1.create_image(id1, id2, image = Images[0])
	can1.image = Images[0]

def Switch2(S):
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image1 = can1.create_image(id1, id2, image = Images[0])
	can1.image = Images[0]

def Routeur():
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image2 = can1.create_image(id1, id2, image = Images[1])
	can1.image = Images[1]
	
def Routeur2(R):
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image2 = can1.create_image(id1, id2, image = Images[1])
	can1.image = Images[1]
	
def PC():
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image3 = can1.create_image(id1, id2, image = Images[2])
	can1.image = Images[2]
	
def PC2(P):
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image3 = can1.create_image(id1, id2, image = Images[2])
	can1.image = Images[2]
	
def Telephone():
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image4 = can1.create_image(id1, id2, image = Images[3])
	can1.image = Images[3]
	
def Telephone2(T):
	id1 = Zone1.get()
	id2 = Zone2.get()
	Image4 = can1.create_image(id1, id2, image = Images[3])
	can1.image = Images[3]
	
root = Tk()
root.title('Application réseau')
root.geometry('720x720')
root.bind("<S>", Switch2)
root.bind("<R>", Routeur2)
root.bind("<P>", PC2)
root.bind("<T>", Telephone2)


SwitchImage = PhotoImage(file='SwitchImage.png')
RouteurImage = PhotoImage(file='RouteurImage.png')
PcImage = PhotoImage(file='PcImage.png')
TelephoneImage = PhotoImage(file='TelephoneImage.png')
SwitchImageBouton = PhotoImage(file='SwitchImageBouton.png')
RouteurImageBouton = PhotoImage(file='RouteurImageBouton.png')
PcImageBouton = PhotoImage(file='PcImageBouton.png')
TelephoneImageBouton = PhotoImage(file='TelephoneImageBouton.png')
Images = [SwitchImage, RouteurImage, PcImage, TelephoneImage]
ImagesBouton = [SwitchImageBouton, RouteurImageBouton, PcImageBouton, TelephoneImageBouton ]

font = font.Font(weight="bold")


can = Canvas(root, width=150, height=720, bg='ivory')
can.pack(side=LEFT)
can1 = Canvas(root, width=10000, height=720, bg='white')
can1.bind("<Double-Button-1>", suppr)
can1.bind("<ButtonPress-1>", Cable)
can1.pack(side=RIGHT)
can1.old_coords = None

Zone1 = Entry(can, width=10)
Zone1.pack()

Zone2 = Entry(can, width=10)
Zone2.pack()

Label0 = Label(can, text='Choisir les coordonnées', width=120, height=1, fg='blue')
Label0.pack()

Label01 = Label(can, text='de vos objets', width=120, height=1, fg='blue')
Label01.pack()

Label1 = Label(can, text='Menu', width=150, height=3,borderwidth=2, bg='red', justify=CENTER)
Label1['font'] = font
Label1.pack()

Label2 = Label(can, text='Double clic pour supprimer ', width=120, height=1, fg='blue')
Label2.pack()

Label3 = Label(can, text='un seul objet uniquement ', width=120, height=1, fg='blue')
Label3.pack()

Label4 = Label(can, text='Clique Gauche pour choisir', width=120, height=1, fg='blue')
Label4.pack()

Label5 = Label(can, text='où mettre les câbles', width=120, height=1, fg='blue')
Label5.pack()

B1 = Button(can, width=170, bg='gray', command = Switch, text='Switch ', image = ImagesBouton[0], compound = RIGHT)   #Switch
B1.pack(side=LEFT)
B1['font'] = font

B2 = Button(can, height = 2, width=150, bg='gray', text = 'Client', command = affiche)
B2.pack(side=LEFT)
B2['font'] = font

B3 = Button(can, bg='gray', width=170, text = 'Routeur ', command = Routeur, image = ImagesBouton[1], compound=RIGHT)   
B3.pack(side=LEFT)
B3['font'] = font

B4 = Button(can, text='Tout supprimer', height=2, width=150, bg='gray', command = Tsuppr)
B4.pack(side=LEFT)
B4['font'] = font


can.create_window(35, 125, window=Zone1)
can.create_window(115, 125, window=Zone2)
can.create_window(67, 72, window=Label0)
can.create_window(67, 88, window=Label01)
can.create_window(67, 30, window=Label1)
can.create_window(76, 644, window=Label2)
can.create_window(75, 578, window=Label4)
can.create_window(66, 594, window=Label5)
can.create_window(76, 661, window=Label3)
can.create_window(66, 200, window=B1)
can.create_window(66, 350, window=B2)
can.create_window(66, 500, window=B3)
can.create_window(66, 698, window=B4)



root.mainloop()
