#coding:utf-8
# fichier main_pendu.py

'''
CODES COULEUR DU DESSIN POUR RESTER DANS LES TONS :
-------------------------------------------------
#84161A
#B41A1E
#D7351B
#E95C35
#FFE990

POLICE IDENTIQUE DANS TOUT LE JEUX A INSTALLER SUR SON ORDI :
------------------------------------------------------------
https://www.dafont.com/fr/mystery-day.font?fpp=200&text=Bienvenue+dans+le+jeux+du+pendu+%21

'''
# -------- LES IMPORTS -----------

import module_samia as ms
import module_abder as ma
import module_jarfar as mj
import module_sikou as mk

import module_wahib as mw       #
from tkinter import *           # Pour l'interface graphique GUI
from tkinter import messagebox  # POUR L'affichage des popup windows
import pygame                   # J'importe pygame pour gérer le son en boucle








# ----------------- INITIALISATION ---------------------

fen = Tk()                      # INITIALISATION DE TKINTER
pygame.mixer.init()             # INITIALISATION DE PYGAME




fen.title("Jeux du pendu sur TKinter")
fen.resizable(width=False, height=False)  # Empeche le redimentionnement L x H fixé à 800 x 600
#fen.iconbitmap("src/IcoPendu9.ico")      # ATTENTION CETTE LIGNE CASSE LE CENTRAGE DE LA GUI DANS L'ECRAN







# -----------------FONCTIONS ---------------------
#-------------------------------------------------



def aide_message_pop():
    ''' J'affiche un Message d'aide lorsque je clique sur le bouton aide '''
    can = Canvas(fen, width=150, bg="#84161A", highlightthickness=0 )
    can.place(x=630, y=60)


    btn2 = Button(can,
                font=("Mystery-Day",13),
                text='X',
                bg="#84161A",
                fg="#FFE990",
                command = can.destroy)
    #btn2.pack(side=TOP, padx= 20)
    btn2.grid(row=0, column=3)

    messag_aide = Message(can,
                        width = 140,
                        font=("Mystery-Day",13),
                        #bd=10,
                        #relief=RIDGE, # SUNKEN, RAISED, GROOVE et RIDGE
                        bg="#84161A",
                        fg="#FFE990",
                        text="Ce jeux consiste à trouver un mot avec un nombre de tentative limité, Ce jeux consiste à trouver un mot avec un nombre de tentative limité,Ce jeux consiste à trouver un mot avec un nombre de tentative limité")
    #messag_aide.place(x=620, y=60)
    messag_aide.grid(row=1, columnspan =3)
    


def aide_showinfo(): # AFFICHE LES REGLES DU JEUX
    ''' J'affiche un popup windows grace à showinfo via messagebox de tkinter '''
    messagebox.showinfo("Règles du jeux", "Ce jeux consiste à trouver un mot avec un nombre de tentative limité, Ce jeux consiste à trouver un mot avec un nombre de tentative limité,Ce jeux consiste à trouver un mot avec un nombre de tentative limité")



# -- DEBUT --
def pop_ask_cut_window_et_son():

    ''' SI JE FERME MA FENETRE, LE SON JOUE ENCORE. POUR EMPECHER CELA, CAPTURER L'EVENEMENT DE
    FERMETURE DE FENETRE (LA CROIX) POUR MODIFIER LA PROCEDURE DE FERMETURE,
    EN APPELANT UNE FONCTION QUI VA QUITTER PYGAME protocol() '''

    m = messagebox.askyesno("Fermeture fenêtre","Tu veux vraiment arrêter la partie ?")
    if m == YES:
        pygame.quit() # POUR COUPER LE SON PYGAME
        fen.destroy() # POUR QUITTER
    else:
        messagebox.showinfo("Re :-)","Content de te revoir")

fen.protocol("WM_DELETE_WINDOW", pop_ask_cut_window_et_son) # WM pour Windows Manager

# SANS LE CODE CI-DESSUS, LE SON JOUERAI ENCORE A LA FERMETURE DE LA FENTRE
# -- FIN --






































# CENTRER LA FENETRE PRINCIPALE TKINTER AU MILIEU DE L'ECRAN
#-----------------------------------------------------------
largeur_ecran = int(fen.winfo_screenwidth())
hauteur_ecran = int(fen.winfo_screenheight())
largeur_fenetre = 798
hauteur_fenetre = 670

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

geo = "{}x{}+{}+{}".format(largeur_fenetre,  hauteur_fenetre,  posX,  posY)

fen.geometry(geo)








# CI-DESSOUS CANEVAS FENETRE IMAGE D'ARRIERE PLAN - ETAPE 9 PERSONNAGE PENDU
#---------------------------------------------------------------------------

pendu9 = Canvas(fen, width=800, height=670)
imgPendu9 = PhotoImage(file="src/pendu9.png")
pendu9.create_image(0,0, anchor=NW, image=imgPendu9)
pendu9.place(x=-2, y=0)








#---------- MENU -----------

menu_bar = Menu(fen)


# SOUS ONGLETS DEROULANTS LIES AU  1er LABEL
derouler_1 = Menu(menu_bar, tearoff=0 ) # tearoff=0 m'ote cette barre moche qui s'affiche en haut du menu déroulant
derouler_1.add_command(label="Jouer")  # COMMAND A VENIR
derouler_1.add_command(label="Quitter", command= pop_ask_cut_window_et_son )

menu_bar.add_cascade(label="Jouer/Quitter", menu=derouler_1, activeforeground="#84161A")    # 1er label



derouler_2 = Menu(menu_bar, tearoff = 0 )
derouler_2.add_command(label="Trop façile, 9 tentatives et on t'affiche la 1ere et la dernière ou 2 lettres au hasard")  # COMMAND A VENIR
derouler_2.add_command(label="Moyen car on retire la 1ere et la derniere")  # COMMAND A VENIR
derouler_2.add_command(label="Dificile car tu n'as que 5 tentatives")  # COMMAND A VENIR

menu_bar.add_cascade(label="Niveaux", menu= derouler_2)                                       # 2e  label



derouler_3 = Menu(menu_bar, tearoff = 0 )
derouler_3.add_command(label="Règles du jeux", command = aide_showinfo) # AFFICHER UN POPUP
derouler_3.add_command(label="Définition du pendu wikipedia", command = mw.wikiHelp)

menu_bar.add_cascade(label="Aide", menu = derouler_3)                # 3e  label



fen.config(menu= menu_bar)










# --------------------------------- FRAME DU HAUT / BOUTONS ET TITRE---------------------------------

frameHaut = Frame(fen, bg="#84161A")
frameHaut.pack(side=TOP, pady=15) # fill=X


# BOUTON NIVEAUX A GAUCHE #
'''
# BOUTON SEUL
bouton_niveau  = Button(frameHaut, text="Niveaux", font=("Mystery-Day",15), bd=4, bg="#84161A", fg="#FFE990", state = DISABLED)
bouton_niveau.grid(row=0, column=0)
'''

btn_niveau_menu = Menubutton(frameHaut,
                            text="Niveaux",
                            font=("Mystery-Day",15),
                            bd=0,
                            bg="#84161A",
                            fg="#FFE990")
btn_niveau_menu.menu = Menu(btn_niveau_menu,
                            tearoff = 0,
                            font=("Mystery-Day",8),
                            bd=0,
                            bg="#84161A",
                            fg="#FFE990")
btn_niveau_menu["menu"] = btn_niveau_menu.menu
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
btn_niveau_menu.menu.add_checkbutton(label = "Trop façile", variable = v1)
btn_niveau_menu.menu.add_checkbutton(label = "Moyen", variable = v2)
btn_niveau_menu.menu.add_checkbutton(label = "Difficile", variable = v3)
btn_niveau_menu.grid(row=0, column=0, padx=3)


# BOUTON JOUER A GAUCHE #
bouton_jouer  = Button(frameHaut, text="Jouer", font=("Mystery-Day",15), bd=4, bg="#84161A", fg="#FFE990")
bouton_jouer.grid(row=0, column=1)


# TITRE AU CENTRE
label_titre = Label(frameHaut, text="  Bienvenue dans le jeux du pendu !  ", font=("Mystery-Day",25), bg="#84161A", fg="#FFE990")
label_titre.grid(row=0, column=2)


# BOUTON AIDE A DROITE
boutonAide = Button(frameHaut,
                    text="Aide",
                    font=("Mystery-Day",15),
                    bd=4, bg="#84161A",
                    fg="#FFE990",
                    command = aide_message_pop)
boutonAide.grid(row=0, column=3, padx=5)


# BOUTON QUITTER A DROITE
boutonQuitter = Button(frameHaut, text="Quitter", font=("Mystery-Day",15), bd=4, bg="#84161A", fg="#FFE990", command = pop_ask_cut_window_et_son )
boutonQuitter.grid(row=0, column=4)








# --------------------------------- BOUTONS RADIO SON ---------------------------------


frameRADIO = Frame(fen, bg="#84161A")
frameRADIO.place(x = 20, y = 60)

def son1():
    pygame.mixer.music.load("src/hell.mp3") # shirojyuu.mp3  # jincheng.mp3
    pygame.mixer.music.set_volume(0.6) # volume entre 0 et 1  via  0.1  0.2  0.3  etc.
    pygame.mixer.music.play(-1)        # L'argument -1 faire en sorte d'écouter en boucle

def son2():
    pygame.mixer.music.load('src/crim.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def son3():
    pygame.mixer.music.load('src/blade.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def stop():
    pygame.mixer.music.stop()


v = StringVar() # Création de la variable
v.set('son')    # Cette ligne coche le 1er button par défaut sinon aucun des boutons n'est coché

r1 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                text="son1",
                value="son1",
                variable = v,
                command = son1)
r1.grid(row = 0, column = 0, padx = 2)


r2 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                text="son2",
                value="son2",
                variable = v,
                command = son2)
r2.grid(row = 0, column = 1, padx = 2)

r3 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                text="son3",
                value="son3",
                variable = v,
                command = son3)
r3.grid(row = 0, column = 2, padx = 2)

r4 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                text="cut",
                value="stop",
                variable = v,
                command = stop)
r4.grid(row = 0, column = 4, padx = 2)








# -------------------- FRAME DU BAS / MOT CACHE + CLAVIER -------------------


# ---------- LABEL MOT CACHE ****** ---------

frame_mot_clavier = Frame(fen, bg="black", width = 20)
frame_mot_clavier.pack(side = BOTTOM, pady= 12) # expand=TRUE pour centrer en hauteur


def recup_lettre():
    #mon_label.set()
    label_mot.config( text = btn_clavier['text'] )


#var = StringVar()
label_mot = Label(frame_mot_clavier,
                    text = "",
                    #textvariable=var,
                    #width = 10,
                    height = 1,
                    font=("Mystery-Day",25),
                    bd=5,
                    relief=SUNKEN, # SUNKEN, RAISED, GROOVE et RIDGE
                    bg="black",
                    fg="#FFE990")

#var.set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

label_mot.grid(row = 0, columnspan = 26, ipadx = 50)







# ------------------ CLAVIER 1 ---------------

# STOCKAGE DE L'ALPHABET DANS UNE LISTE
abcd = []
for i in range(26):
    abcd += chr(65+i)



# AFFICHAGE ALPHABET DANS TKINTER
for i in range(26):
    '''Je récupère chaque lettre de la liste abcd pour un affichage en bouton '''
    btn_clavier = Button(frame_mot_clavier,
                        width = 2,
                        font=("Mystery-Day",15),
                        text= abcd[i],
                        bg="#84161A",
                        fg="#FFE990",
                        command = recup_lettre)
    btn_clavier.grid(row=1, column=i)






# ------------------------- CopyLeft ------------------------
copyLeft = Label(fen,
                font=("Mystery-Day",7),
                text="CopyLeft : Greta 78 - ABDERRAHIM JARFAR SAMIA SIKOU WAHIB - son1/hell - son2/crim - son3/blade",
                bg="black",
                fg="#FFE990")

copyLeft.place( x=3, y=658)








# ------------------------- FIN ------------------------
fen.mainloop()

print("FIN")














