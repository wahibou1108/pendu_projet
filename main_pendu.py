#coding:utf-8
# fichier main_pendu.py

'''
ZONE DE TEST FONCTION :
-------------------------------------------------
MAIS PENSER A LES INTEGRER DANS LA MESURE DU POSSIBLE DANS VOS MODULE RESPECTIFS
CECI AFIN DE GARDER UN CODE AUSSI LISIBLE QUE POSSIBLE


CODE COULEUR DU DESSIN POUR RESTER DANS LES TONS :
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

def fonc_aide():
    ''' J'affiche un Message d'aide lorsque je clique sur le bouton aide '''
    messag_aide = Message(fen,
                        width = 150,
                        font=("Mystery-Day",13),
                        bd=10,
                        relief=RIDGE, # SUNKEN, RAISED, GROOVE et RIDGE
                        bg="#84161A",
                        fg="#FFE990",
                        text="Ce jeux consiste à trouver un mot avec un nombre de tentative limité, Ce jeux consiste à trouver un mot avec un nombre de tentative limité,Ce jeux consiste à trouver un mot avec un nombre de tentative limité")
    messag_aide.place(x=610, y=50)




































# -------- J'IMPORTE CHAQUE MODULE DE MA SCRUM -----------

import module_samia as ms
import module_abder as ma
import module_wahib as mw
import module_jarfar as mj
import module_sikou as mk

# ------------------ J'IMPORTE TKINTER -------------------

from tkinter import *

# ------------------------- DÉBUT ------------------------
# ----------------- TKINTER COMMENCE ICI -----------------

fen = Tk() # fen veut dire fenêtre

fen.title("Jeux du pendu sur TKinter")
fen.iconbitmap("src/IcoPendu9.ico")
fen.resizable(width=False, height=False)






# CENTRER LA FENETRE PRINCIPALE TKINTER AU MILIEU DE L'ECRAN
#-----------------------------------------------------------
largeur_ecran = int(fen.winfo_screenwidth())
hauteur_ecran = int(fen.winfo_screenheight())
largeur_fenetre = 800
hauteur_fenetre = 670

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

geo = "{}x{}+{}+{}".format(largeur_fenetre,  hauteur_fenetre,  posX,  posY)

fen.geometry(geo)






# CANEVAS FENETRE IMAGE D'ARRIERE PLAN
#-------------------------------------
canvArrPlan = Canvas(fen, width=800, height=670)                # LA TAILLE DE MON CANEVAS
imgArrierePlan = PhotoImage(file="src/pendu0.png")              # .zoom(2)
canvArrPlan.create_image(0,0, anchor=NW, image=imgArrierePlan)  # anchor défini de point de départ NWest NEst SW SE de l'img
canvArrPlan.place(x=0, y=0)                                     # LA POSITION X Y DE MON CANEVAS

# CI-DESSOUS ETAPE 9 , PERSONNAGE COMPLETEMENT PENDU
'''
pendu9 = Canvas(fen, width=800, height=670)
imgPendu9 = PhotoImage(file="src/pendu9.png")
pendu9.create_image(0,0, anchor=NW, image=imgPendu9)
pendu9.place(x=-1, y=0)

'''






#---------- MENU ----------

menu_bar = Menu(fen)


# SOUS ONGLETS DEROULANTS LIES AU  1er LABEL
derouler_1 = Menu(menu_bar, tearoff=0 ) # tearoff=0 m'ote cette barre moche qui s'affiche en haut du menu déroulant
derouler_1.add_command(label="Jouer")  # COMMAND A VENIR
derouler_1.add_command(label="Quitter", command= fen.destroy )

menu_bar.add_cascade(label="Jouer/Quitter", menu=derouler_1, activeforeground="#84161A")    # 1er label



derouler_2 = Menu(menu_bar, tearoff = 0 )
derouler_2.add_command(label="Trop façile, 9 tentatives et on t'affiche la 1ere et la dernière ou 2 lettres au hasard")  # COMMAND A VENIR
derouler_2.add_command(label="Moyen car on retire la 1ere et la derniere")  # COMMAND A VENIR
derouler_2.add_command(label="Dificile car tu n'as que 5 tentatives")  # COMMAND A VENIR

menu_bar.add_cascade(label="Niveau", menu= derouler_2)                                       # 2e  label



derouler_3 = Menu(menu_bar, tearoff = 0 )
derouler_3.add_command(label="Règles du jeux", command = fonc_aide) # AFFICHER UN POPUP
derouler_3.add_command(label="Définition du pendu wikipedia", command = mw.wikiHelp)

menu_bar.add_cascade(label="Aide", menu = derouler_3)                # 3e  label



fen.config(menu= menu_bar)








# --------------------------------- FRAME DU HAUT / BOUTONS ET TITRE---------------------------------

frameHaut = Frame(fen, bg="#84161A")
frameHaut.pack(side=TOP, pady=5) # fill=X


# BOUTON NIVEAUX A GAUCHE #
bouton_niveau  = Button(frameHaut, text="Niveau", font=("Mystery-Day",15), bd=4, bg="#84161A", fg="#FFE990", state = DISABLED)
bouton_niveau.grid(row=0, column=0)

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
                    command = fonc_aide)
boutonAide.grid(row=0, column=3)



# BOUTON QUITTER A DROITE
boutonQuitter = Button(frameHaut, text="Quitter", font=("Mystery-Day",15), bd=4, bg="#84161A", fg="#FFE990", command=fen.destroy)
boutonQuitter.grid(row=0, column=4)







# --------------------------------- FRAME DU BAS / ALPHABET ---------------------------------

frameBas = Frame(fen)
frameBas.pack(side = BOTTOM)

# STOCKAGE DE L'ALPHABET DANS UNE LISTE
abcd = []
for i in range(26):
    abcd += chr(65+i)

# print(abcd) # DEBUG

for i in range(26):
    ''' Je récupère chaue lettre de la liste abcd pour un affichage en bouton '''
    boutons_abcd = Button(frameBas,
                        font=("Mystery-Day",15),
                        text= abcd[i],
                        bg="#84161A",
                        fg="#FFE990")
    boutons_abcd.grid(row=3, column=i)













# ------------------------- FIN ------------------------
fen.mainloop()














