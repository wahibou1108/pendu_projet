# fichier module_wahib.py

import webbrowser               # POUR CREER UN EVENEMENT ENTRE LE BOUTON ET L'AFFICHAGE D'UNE PAGE WEB
from tkinter import *           # Pour l'interface graphique GUI
from tkinter import messagebox  # POUR L'affichage des popup windows
import pygame                   # J'importe pygame pour gérer le son en boucle
import random                   # POUR CHOISIR UN MOT DANS UNE LISTE VIA CHOICE()







# ------------ MENU DEROULANT ------------

def wikiHelp(): # CETTE FONCTION SE TROUVE DANS LE
    return webbrowser.open_new("https://fr.wikipedia.org/wiki/Le_Pendu_(jeu)")


def aide_showinfo(): # AFFICHE LES REGLES DU JEUX VIA UN POPUP WINDOWS
    ''' J'affiche un popup windows grace à showinfo via messagebox de tkinter '''
    messagebox.showinfo(title = "Aide", message = "Ce jeux consiste à trouver un mot avec un nombre de tentative limité.\n\
- Level 1 par défaut te donne droit à 9 vies et deux indices.\n\
- Level 2 ne te donne pas d'indices.\n\
- Level 3 te donne quatre vies seulement")







# ------------ RADIO BOUTONS SOUND --------------

def mute():
    pygame.mixer.music.stop()



def son1():
    pygame.mixer.music.load("src/sound_hell.mp3")
    pygame.mixer.music.set_volume(0.2)      # volume entre 0 et 1  via  0.1  0.2  0.3  etc.
    pygame.mixer.music.play(-1)             # L'argument -1 faire en sorte d'écouter en boucle

def son2():
    pygame.mixer.music.load('src/sound_crim.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def son3():
    pygame.mixer.music.load('src/sound_blade.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def son4():
    pygame.mixer.music.load('src/sound_shirojyuu.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def son5():
    pygame.mixer.music.load('src/sound_jincheng.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)



def son6():
    pygame.mixer.music.load('src/sound_gagne.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)         # -1 en boucle   et   0 une fois

def son7():
    pygame.mixer.music.load('src/sound_perdu.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)

def son8():
    pygame.mixer.music.load('src/sound_faudel.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)

def son9():
    pygame.mixer.music.load('src/sound_clic.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)







if __name__ == "__main__":
    pass














