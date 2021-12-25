#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      FRsaitam
#
# Created:     25/12/2021
# Copyright:   (c) FRsaitam 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import ttkthemes as td #you should first install ttkthemes using bash command "pip install ttkthemes"
from tkinter import ttk
import pygame
from tkinter import messagebox



MyWindow = td.ThemedTk()
MyWindow.get_themes()
MyWindow.set_theme('black') #i prefer the "radiance", "black" and "aquativo" theme
MyWindow.title("Jeud du pendu")
MyWindow.geometry("800x600")
MyWindow.config(bg='whitesmoke')
MyWindow.resizable(0, 0)

def select(value):

    for elem in range(len(buttons)-1):
        if value==buttons[elem]:
            textarea.insert(INSERT, buttons[elem])

    if value=="Back":
        i=textarea.get(1.0, END) #it is going to get the whole text from the start including the cursor
        newText=i[:-2] #it will delet the cursor and the last tapedletter
        textarea.delete(1.0, END)#it will delet the whole text from sthe start
        textarea.insert(INSERT, newText)

    textarea.focus_set()

#Lire et stopper un son MP3
pygame.mixer.init()
def play():
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

#Quitter la fenetre MyWindow
def Quitter():
   if messagebox.askokcancel("Quit", "Do you really wish to exit?"):
    pygame.quit()
    MyWindow.destroy()

#afficher la lettre cliqué par le clavier
def cliquer(event):
    label1.config(text=event.char)




frame1=Frame(MyWindow)
frame1.pack(side=TOP,fill=X)

frame2=Frame(MyWindow)
frame2.pack(side=TOP, fill=X)


#Création d'un menu déroulante pour le choix des catégories
m=Menu(frame1)
MyWindow.config(menu=m)
submenu=Menu(m)
m.add_cascade(label='Réglage',menu=submenu, activebackground ='pink', activeforeground ='green')
submenu.add_command(label= "1: jouer la musique", command = play, activebackground ='pink', activeforeground ='green')
submenu.add_command(label = "2: Arrêter la musique", command = stop, activebackground ='pink', activeforeground ='green')
submenu.add_separator()
submenu.add_command(label = "3: Quitter", command = Quitter, activebackground ='pink', activeforeground ='green')


# **** ToolBar *******

toolbar=Frame(frame1,bg='grey')
toolbar.pack(side=TOP,fill=X)


#création d'un titre en dessus du l'aperçu du text "The displayed text"
titleLabel = Label(toolbar, text='The word to be guessed', font=('arial', 15, 'bold'), bg='whitesmoke', fg='white')
titleLabel.config(bg="gray")
titleLabel.pack(padx=2)


#Création de l'espace du text saisis #relief=SUNKEN est pour le choix de la bordure
textarea=Text(toolbar, font=('arial', 15, 'bold'), height=1, width=15, wrap=WORD, bd=8, relief='ridge')
textarea.config(bg="Red")
textarea.pack(padx=2)



# ***** Clavier avec sortie en text ******

#La liste des boutons du clavier
buttons = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', '-', 'Back']



varRow = 3
varColumn = 0

for button in buttons:

    command = lambda x=button: select(x) #Lambda is a keyword
    if varColumn < 9:
        ttk.Button(frame2, text=button, command=command, width=12).grid(row=varRow, column=varColumn)
        style = ttk.Style()
        style.configure('TButton', background='Red')

    varColumn += 1

    if varColumn >= 9:
        varColumn = 0
        varRow += 1



# **** StatusBar ******************
#Création d'une image en arriere plan
filename = PhotoImage(file = 'pendu9.png') #PhotoImage n'accepte que format .png
background_label = ttk.Label(MyWindow, image=filename)
status= background_label
status.pack(side=TOP, fill=X, padx=2)


# affichage de la fenêtre principale
MyWindow.mainloop()