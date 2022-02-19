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

#import module_samia as ms      # RETIRER LE # POUR TESTER L'ALGO PENDU EN LIGNE DE COMMANDE
#import module_abder as ma
#import module_jarfar as mj
#import module_sikou as mk
import module_wahib as mw       #

from tkinter import *           # Pour l'interface graphique GUI
from tkinter import messagebox  # POUR L'affichage des popup windows
import pygame                   # J'importe pygame pour gérer le son en boucle
import random                   # POUR CHOISIR UN MOT DANS UNE LISTE VIA CHOICE()
from unidecode import unidecode # pour remplacer les caracteres avec accents lorsque j'appele une liste de mots via random
import os








# ------------- INITIALISATION TK - TITRE - ET REDIMENTIONNEMENT FENETRE  -------------

fen = Tk()                      # INITIALISATION DE TKINTER
pygame.mixer.init()             # INITIALISATION DE PYGAME PRINCIPALEMENT POUR LE SON




fen.title("Jeux du pendu sur TKinter")
fen.resizable(width=False, height=False)  # Empeche le redimentionnement L x H fixé à 800 x 600
#fen.iconbitmap("src/IcoPendu9.ico")      # ATTENTION CETTE LIGNE CASSE LE CENTRAGE DE LA GUI DANS L'ECRAN
fen.configure(bg="#84161A")               # COMMENTER CETTE LIGNE POUR MIEUX CONTROLER L'EMPLACEMENT DE L'IMAGE      # "#84161A"








#-------------------------------------------------------------------------------------------------|
# ----------------- LES FONCTIONS --- D'AUTRES SONT DANS MODULE_WAHIB.PY AS MW -------------------|
#-------------------------------------------------------------------------------------------------|


def aide_message_pop(): # AFFICHE UN ENCART MESSAGE DANS TK
    # J'affiche un Message d'aide lorsque je clique sur le bouton aide
    can = Canvas(fen, width=150, bg="#84161A", highlightthickness=0 )
    can.place(x=630, y=50)

    btn2 = Button(can,  # BOUTON X POUR FERMER LE MESSAGE AIDE
                font=("Mystery-Day",8),
                text='X',
                bd=1,
                bg="#84161A",
                fg="#FFE990",
                activebackground = "#E95C35",
                activeforeground = "black",
                command = can.destroy)              # ESSAYER CETTE METHODE --> Comment cacher, récupérer et supprimer les widgets Tkinter
    btn2.grid(row=0, columnspan =3, sticky='we')    # https://www.delftstack.com/fr/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/#grid-forget-m%C3%A9thode-pour-cacher-les-widgets-tkinter-si-le-layout-grid-est-utilis%C3%A9

    messag_aide = Message(can,
                        width = 140,
                        font=("Mystery-Day",13),
                        bg="#84161A",
                        fg="#FFE990",
                        text="Ce jeux consiste à trouver un mot avec un nombre de tentative limité.\n\
- Level 1 par défaut te donne droit à 9 vies et deux indices.\n\
- Level 2 ne te donne pas d'indices.\n\
- Level 3 te donne quatre vies seulement")
    messag_aide.grid(row=1, columnspan =3)





# CETTE FONCTION AFFICHE LES REGLES DU JEUX ET SE SITUE DANS MODULE_WAHIB.PY

# def aide_showinfo():




# -- DÉBUT -- LA fonction ci-dessous a pour but d'arreter
# le son en même temps que la fermeture fenetre via la croix ou le btn quitter --

def pop_ask_cut_window_et_son():

    # SI JE FERME MA FENETRE, LE SON JOUE ENCORE. POUR EMPECHER CELA, CAPTURER L'EVENEMENT DE
    # FERMETURE DE FENETRE (LA CROIX) POUR MODIFIER LA PROCEDURE DE FERMETURE,
    # EN APPELANT UNE FONCTION QUI VA QUITTER PYGAME --> protocol()

    m = messagebox.askyesno("Fermeture fenêtre","Tu veux vraiment arrêter la partie ?")

    if m == YES:

        pygame.quit() # POUR COUPER LE SON PYGAME
        fen.destroy() # POUR QUITTER

    else:

        messagebox.showinfo("Re :-)","Content de te revoir")

# -- FIN -- SANS LE CODE CI-DESSUS, LE SON JOUERAI ENCORE A LA FERMETURE DE LA FENTRE

fen.protocol("WM_DELETE_WINDOW", pop_ask_cut_window_et_son) # WM pour Windows Manager                           # -- PROTOCOLE --








def restart():
    pygame.quit()                         # CETTE LIGNE EMPECHE LE SON DE CONTINUER APRES LA FERMETURE DE LA FENETRE
    fen.destroy()                         # CETTE LIGNE ARRETE L'APPLICATION
    os.startfile("main_pendu.pyw")            # CETTE LIGNE RELANCE L'APPLICATION.
































# ------------- CENTRER LA FENETRE PRINCIPALE TKINTER AU MILIEU DE L'ECRAN  -------------


largeur_ecran = int(fen.winfo_screenwidth())
hauteur_ecran = int(fen.winfo_screenheight())
largeur_fenetre = 800
hauteur_fenetre = 710

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)
fen.geometry( f"{largeur_fenetre}x{hauteur_fenetre}+{posX}+{posY}" )














# --------------------------------- MENU DEROULANT ---------------------------------

menu_bar = Menu(fen)


# SOUS ONGLETS DEROULANTS LIES AU  1er LABEL
derouler_1 = Menu(menu_bar, tearoff=0 )                                         # tearoff=0 m'ote cette barre moche qui s'affiche en haut du menu déroulant
derouler_1.add_command(label="Jouer", command = restart)                        # cette fonction reset le jeux via os et coupe le son
derouler_1.add_command(label="Quitter", command = pop_ask_cut_window_et_son )   #  command= fen.destroy

menu_bar.add_cascade(label="Jouer/Quitter", menu = derouler_1, activeforeground = "#84161A")    # 1er label



derouler_2 = Menu(menu_bar, tearoff = 0 )
derouler_2.add_command(label="Level 2 (aucun indice)")                          # COMMAND A VENIR
derouler_2.add_command(label="Level 3 (4 tentatives)")                          # COMMAND A VENIR

menu_bar.add_cascade(label="Niveaux", menu= derouler_2)                                       # 2e  label



derouler_3 = Menu(menu_bar, tearoff = 0 )
derouler_3.add_command(label="Règles de ce pendu", command = mw.aide_showinfo) # AFFICHER UN POPUP
derouler_3.add_command(label="Définition du pendu wikipedia", command = mw.wikiHelp)

menu_bar.add_cascade(label="Aide", menu = derouler_3)                                       # 3e  label



fen.config(menu= menu_bar)













# --------------------- RADIO BOUTONS SON --- FONCTIONS DANS MODULE_WAHIB.PY ---------------------

frameRADIO = Frame(fen, bg="#84161A")
frameRADIO.place(x = 180, y = 41, anchor=NW)


v = StringVar() # Création de la variable
v.set('mute')    # Cette ligne coche le 1er button par défaut sinon aucun des boutons n'est coché

r0 = Radiobutton(frameRADIO,            # RADIOBUTTON STOP COCHE PAR DEFAUT
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="mute",
                value="mute",
                variable = v,
                command = mw.mute)          # FONCTION DANS MODULE_WAHIB.PY
r0.grid(row = 0, column = 0, padx = 2)

r1 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="1",
                value="son1",
                variable = v,
                command = mw.son1)          # FONCTION DANS MODULE_WAHIB.PY
r1.grid(row = 0, column = 1, padx = 2)

r2 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="2",
                value="son2",
                variable = v,
                command = mw.son2)          # FONCTION DANS MODULE_WAHIB.PY
r2.grid(row = 0, column = 2, padx = 2)

r3 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="3",
                value="son3",
                variable = v,
                command = mw.son3)          # FONCTION DANS MODULE_WAHIB.PY
r3.grid(row = 0, column = 3, padx = 2)

r4 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="4",
                value="son4",
                variable = v,
                command = mw.son4)          # FONCTION DANS MODULE_WAHIB.PY
r4.grid(row = 0, column = 4, padx = 2)

r5 = Radiobutton(frameRADIO,
                font=("Mystery-Day",10),
                bg="#84161A",
                fg="#E95C35",
                activebackground = "#84161A",
                activeforeground = "#FFE990",
                text="5",
                value="son5",
                variable = v,
                command = mw.son5)          # FONCTION DANS MODULE_WAHIB.PY
r5.grid(row = 0, column = 5, padx = 2)













# ----------------- FRAME HAUT ----------------------

frameHaut = Frame(fen, bg="#84161A")
frameHaut.pack(fill='both', pady=3) # fill=X

# ----------------- FRAME HAUT ----------------------


# BOUTON NIVEAUX A GAUCHE #

# BOUTON SEUL
bouton_niveau2  = Button(frameHaut,
                        text="L2",
                        font=("Mystery-Day",15),
                        bd=1,
                        bg="#84161A",
                        fg="#FFE990",
                        activebackground = "#E95C35",
                        activeforeground = "black",
                        width = 4,
                         )
bouton_niveau2.grid(row=0, column=0, padx=1)



bouton_niveau3  = Button(frameHaut,
                       text="L3",
                       font=("Mystery-Day",15),
                       bd=1,
                       bg="#84161A",
                       fg="#FFE990",
                       activebackground = "#E95C35",
                       activeforeground = "black",
                       width = 4,
                        )                       # cette fonction reset le jeux via os et coupe le son
bouton_niveau3.grid(row=0, column=1, padx=1)




# BOUTON JOUER A GAUCHE
bouton_jouer  = Button(frameHaut,
                       text="Jouer",
                       font=("Mystery-Day",15),
                       bd=1,
                       bg="#84161A",
                       fg="#FFE990",
                       activebackground = "#E95C35",
                       activeforeground = "black",
                       width = 8,
                       command = restart)                       # cette fonction reset le jeux via os et coupe le son
bouton_jouer.grid(row=0, column=2, padx=1)




# TITRE AU CENTRE
label_titre = Label(frameHaut, text=" Bienvenue dans le jeux du pendu ! ", font=("Mystery-Day",24), bg="#84161A", fg="#FFE990")
label_titre.grid(row=0, column=3)




# BOUTON AIDE A DROITE
boutonAide = Button(frameHaut,
                    text="Aide",
                    font=("Mystery-Day",15),
                    bd=1,
                    bg="#84161A",
                    fg="#FFE990",
                    activebackground = "#E95C35",
                    activeforeground = "black",
                    width = 8,
                    command = aide_message_pop)
boutonAide.grid(row=0, column=4, padx=1)


# BOUTON QUITTER A DROITE
boutonQuitter = Button(frameHaut,
                        text="Quitter",
                        font=("Mystery-Day",15),
                        bd=1,
                        bg="#84161A",
                        fg="#FFE990",
                        width = 8,
                        activebackground = "#E95C35",
                        activeforeground = "black",
                        command = pop_ask_cut_window_et_son ) #  command=fen.destroy
boutonQuitter.grid(row=0, column=5, padx=1)











# -------------- IMAGE DE FOND PERMANANTE VIA LABEL --------------

lab_img = Label( fen, width = 800, height = 430 , bg="#84161A")
lab_img.place(x=-2, y=62, bordermode="outside")
mon_image = PhotoImage( file = "src/pendu0.png" )
lab_img.config(image = mon_image)
lab_img.image = mon_image




# ----- IMAGE PAR DESSUS IMAGE PERMANANTE APPELÉE DANS LE programme_moteur MOTEUR ------

def img_label( jusqua9 ):                                                       # LE PARAMETRE ATTEND LE FUTURE COMPTEUR DE 1 à 9

    lab_img = Label( fen , width = 800, height = 430)
    lab_img.place(x=-2, y=62, bordermode="outside")
    mon_image = PhotoImage( file = f"src/pendu{jusqua9}.png" )
    lab_img.config(image = mon_image)
    lab_img.image = mon_image










# ----------------- FRAME BAS ----------------------
#
frame_label_indice_clavier = Frame(fen, bg="black")
frame_label_indice_clavier.pack(  side=BOTTOM, fill='both', pady=15)


frame_label_indice_clavier.grid_rowconfigure(0, weight=1)
frame_label_indice_clavier.grid_rowconfigure(1, weight=1)
frame_label_indice_clavier.grid_rowconfigure(2, weight=1)


frame_label_indice_clavier.grid_columnconfigure(0, weight=1)
frame_label_indice_clavier.grid_columnconfigure(1, weight=1)
frame_label_indice_clavier.grid_columnconfigure(2, weight=1)

# ----------------- FRAME BAS ----------------------









# -------------------------- DEBUT ALGORITHME PENDU -----------------------------
# -------------------------------------------------------------------------------


print("\n\n--- DÉBUT DE L'ALGORITHME PENDU ---")

chanteur        = ["chebkhaled","chebmami","zaho","idir","chebhasni","chebbilal","takfarinas","chebnadir","cherifa","chebazahouania","rachidtaha","faudel","algerino","chebnasro"]

aleatoire       = unidecode (random.choice(chanteur).upper() )

print("DEBUG : 'aleatoire' -> :",aleatoire)                 # DEBUG : 'aleatoire' -> : CHEBHASNI

bravo = ["_"] * len( aleatoire )

print("DEBUG : 'bravo' :",bravo)                            # DEBUG : 'bravo' : ['_', '_', '_', '_', '_', '_', '_', '_', '_']






# --------- NIVEAU 1 FACILE PAR DEFAUT -->  9 VIES  -->  + 2 INDICES -----------OK LEVEL 1 FACILE PAR DEFAUT

niveau_1_facile = aleatoire[0] + (len(aleatoire)-2)* '_ ' + aleatoire[-1]

print("DEBUG : 'niveau_1_facile' -> :", niveau_1_facile)    # UN indice




# --------- NIVEAU 2 MOYEN  -->  9 VIES  -->   PAS D'INDICES -------------------A FAIRE - PAR EXEMPLE COMMENCER LE PENDU A L'IMAGE 3 ET DESACTIVER LE BOUTON INDICE SI LE CHOIX EST PORTE SUR LE LEVEL 2

niveau_2_moyen = ' '.join(bravo)

print("DEBUG : 'niveau_2_moyen' -> :", niveau_2_moyen)      # PAS d'indice



# --------- NIVEAU 3 DIFFICILE  -->  4 VIES  -->  PAS D'INDICES ----------------









# ICI AFFICHER DYNAMIQUEMENT LE TITRE DE LA LISTE DE MOT QUE RANDOM.RANDINT CHOISIRA

label_indice_liste = Label( fen, text="Chanteur raï".upper(), width = 22, font=("Mystery-Day",15), bg="black", fg="#FFE990" ) # bd=2, relief = SUNKEN,
label_indice_liste.place(x=5, y=600)









# LABEL INDICE --> LE BOUTON DISPARAIT POUR LAISSER PLACE AU LABEL QUI EST PARAMATR2 POUR S'AFFICHER AU MEME EMPLACEMENT

def f_indice():

    label_longeur_lettre = Label(fen, bd=0, text=f"Indice : '{niveau_1_facile}' \n\nCe mot contient {len(aleatoire)} lettres", font=("Mystery-Day",10), bg="black", fg="#FFE990" , width=27 )
    label_longeur_lettre.place(x=590, y=600)

btn_indice = Button(fen, text="? INDICE ?", bd=0, height=2, font=("Mystery-Day",12), bg="black", fg="#FFE990", width=27, command = lambda : [  f_indice(), btn_indice.pack_forget()] )
btn_indice.place(x=590, y=600)








# LABEL MOT UNDERSCORES

def fonc_affiche_mot_cache():                          # CETTE FONCTION EST APPELÉE DANS LE MOTEUR DU programme_moteur
    labelJoue.configure(text = bravo )                 # AFIN DE CONSTAMENT METTRE A JOUR LE LABEL
                                                       # MAIS JE PEUX TOUT SIMPLEMENT APPELER LE LABEL, CA FONCTIONNE AUSSI   -->  abelJoue.configure(text = bravo )

labelJoue = Label( frame_label_indice_clavier, text= bravo, width = 35, height = 2, font=("Mystery-Day",20), bd=2, relief = SUNKEN, bg="black", fg="#FFE990"  ) # J'APPELLE BRAVO MASQUÉ DANS LE LABEL DES LE DÉBUT DE LA PARTIE       # SUNKEN, RAISED, GROOVE et RIDGE
labelJoue.grid( row = 0, column = 1 , pady=0) # sticky="ew"





def f_clic_touche():
    mw.son9()                       # module_wahib.son7()       son du clic touche


















#             COMMENCEMENT DU PROGRAMME PENDU
# -------------------------------------------------------


def disabled_btn(btn): # FONCTION DESACTIVANT LE CLIC SUR UNE LETTRE APRES APPUIS

    global clic_lettre                  # GLOBALE

    clic_lettre = btn['text'].upper()   # JE STOCK LA LETTRE CHOISIE ET EN MAJUSCULE dans la variable clic_lettre

    print(f"\n\nDEBUG : je UPPER() puis DISABLE la touche '{clic_lettre}'")

    if btn['state'] == NORMAL:          # POUR GRISER LES TOUCHES, C'EST CETTE SYNTAXE.
        btn['state'] = DISABLED         # ET LORSQUE JE CLIC SUR UNE TOUCHE, JE LA DISABLE IMMEDITEMENT, AINSI LE PROBLEME EST REGLÉ
                                        # ... CAR ON EST PAS CENSÉ CLIQUER 2 FOIS SUR LA MËME TOUCHE



neuf_coups = 8

quatre_coups = 3

c = 0                                   # GLOBALE

def programme_moteur():

    global c
    vrai = True


    while vrai and c <= neuf_coups :

        f_clic_touche()


        if clic_lettre not in aleatoire and "".join(bravo) != aleatoire:    # MOTEUR 1 : SI LA LETTRE CLIQUÉ N'EST PAS DANS LE MOT ALEATOIRE ALORS TU NE FAIS RIEN MAIS TU COMPTES A REBOURG

            c = c + 1

            print(f"\nDEBUG MOTEUR_1 : '{clic_lettre}' not in '{aleatoire}'. Compteur ='{c}', plus que '{(neuf_coups - c)+1}' tentatives")

            img_label(c)                    # J'APPELLE MA FONCTION IMAGE ET J'AJOUTE UNE NOUVELLE IMAGE PENDU A CHAQUE PERTE

            if c >= 4 :
                mw.son7()                       # module_wahib.son7()       CRI A CHAQUE MAUVAIS COUP

            vrai = False


        if c == 9:
            print(f"\nDEBUG : PERDU PERDU je suis hors jeux !! Compteur = '{c}'")

            mw.son8()                       # SON DE FIN

            vrai = False
            break


        elif clic_lettre in aleatoire:      # MOTEUR 2 : SI LA LETTRE CLIQUÉ EST DANS LE MOT ALEATOIRE ALORS ...

            print(f"\nDEBUG MOTEUR_2 : '{clic_lettre}' in '{aleatoire}'")

            index = 0                       # INDEX QUI VA SERVIR A TRANSFORMER LES UNDERSCORES EN LETTRE AUTANT QU'IL Y A DE LETTRE CLIQUÉES

            for j in aleatoire:

                if j == clic_lettre:

                    bravo[index] = clic_lettre

                    print(f"  DEBUG FOR / IF : bravo[index] m'affiche '{bravo[index]}',\
J'avance à la position '{index}' dans le mot:'{aleatoire}'. Compteur ='{c}'\n")

                    fonc_affiche_mot_cache() # J'AFFICHE LE LABEL A CHAQUE MODIFICATION

                index = index + 1

            print(f'DEBUG : le mot:{"".join(bravo)} correspond il au mot:{aleatoire} ??')

            vrai = False
            #break


        if "".join(bravo) == aleatoire:
            print(f'\nDEBUG : GAGNÉ GAGNÉ!! le mot:{"".join(bravo)} correspond au mot:{aleatoire}. Compteur = {c}')

            mw.son6()                       # module_wahib.son6() gagné

            vrai = False
            break

    print(f"DEBUG__FIN__FONCTION : Compteur = '{c}'")










#----------------------------------------------------
#
#                   FRAMECLAVIER
#
frameClavier = Frame(frame_label_indice_clavier, bg="black")#
frameClavier.grid( row = 1, column = 1, pady=10)
#
#----------------------------------------------------

#--------------------------------------------------------
#                                                       |
#   CI-DESSOUS TROIS FRAM ENFANTS DE   FRAMECLAVIER     |
#  POUR CONSTRUIRE LE CLAVIER AZERTY SUR TROIS LIGNES   |
#                                                       |
frame_A_P = Frame(frameClavier)      #                  |
frame_A_P.grid( row = 0, column = 0 )#                  |
#                                                       |
frame_Q_M = Frame(frameClavier)      #                  |
frame_Q_M.grid( row = 1, column = 0 )#                  |
#                                                       |
frame_W_N = Frame(frameClavier)      #                  |
frame_W_N.grid( row = 2, column = 0 )#                  |
#                                                       |
#--------------------------------------------------------

# LA FONCTION ANONYME LAMBDA ET UNE SOLUTION QUI PERMET DE PASSER UN PARAMETRE A SA PROPRE FONCTION
# CAR COMMAND RECOIT UNIQUEMENT A DES FONCTIONS SANS PARAMETRES. LAMBDA RESOUD CE PROBLEME




btnA = Button(frame_A_P, text="A", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnA), programme_moteur() ] )
btnA.pack(side= LEFT)

btnZ = Button(frame_A_P, text="Z", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnZ), programme_moteur() ] )
btnZ.pack(side= LEFT)

btnE = Button(frame_A_P, text="E", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnE), programme_moteur() ] )
btnE.pack(side= LEFT)

btnR = Button(frame_A_P, text="R", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnR), programme_moteur() ] )
btnR.pack(side= LEFT)

btnT = Button(frame_A_P, text="T", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnT), programme_moteur() ] )
btnT.pack(side= LEFT)

btnY = Button(frame_A_P, text="Y", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnY), programme_moteur() ] )
btnY.pack(side= LEFT)

btnU = Button(frame_A_P, text="U", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnU), programme_moteur() ] )
btnU.pack(side= LEFT)

btnI = Button(frame_A_P, text="I", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnI), programme_moteur() ] )
btnI.pack(side= LEFT)

btnO = Button(frame_A_P, text="O", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnO), programme_moteur() ] )
btnO.pack(side= LEFT)

btnP = Button(frame_A_P, text="P", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnP), programme_moteur() ] )
btnP.pack(side= LEFT)



btnQ = Button(frame_Q_M, text="Q", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnQ), programme_moteur() ] )
btnQ.pack(side= LEFT)

btnS = Button(frame_Q_M, text="S", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnS), programme_moteur() ] )
btnS.pack(side= LEFT)

btnD = Button(frame_Q_M, text="D", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnD), programme_moteur() ] )
btnD.pack(side= LEFT)

btnF = Button(frame_Q_M, text="F", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnF), programme_moteur() ] )
btnF.pack(side= LEFT)

btnG = Button(frame_Q_M, text="G", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnG), programme_moteur() ] )
btnG.pack(side= LEFT)

btnH = Button(frame_Q_M, text="H", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnH), programme_moteur() ] )
btnH.pack(side= LEFT)

btnJ = Button(frame_Q_M, text="J", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnJ), programme_moteur() ] )
btnJ.pack(side= LEFT)

btnK = Button(frame_Q_M, text="K", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnK), programme_moteur() ] )
btnK.pack(side= LEFT)

btnL = Button(frame_Q_M, text="L", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnL), programme_moteur() ] )
btnL.pack(side= LEFT)

btnM = Button(frame_Q_M, text="M", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnM), programme_moteur() ] )
btnM.pack(side= LEFT)



btnW = Button(frame_W_N, text="W", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnW), programme_moteur() ] )
btnW.pack(side= LEFT)

btnX = Button(frame_W_N, text="X", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnX), programme_moteur() ] )
btnX.pack(side= LEFT)

btnC = Button(frame_W_N, text="C", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnC), programme_moteur() ] )
btnC.pack(side= LEFT)

btnV = Button(frame_W_N, text="V", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnV), programme_moteur() ] )
btnV.pack(side= LEFT)

btnB = Button(frame_W_N, text="B", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnB), programme_moteur() ] )
btnB.pack(side= LEFT)

btnN = Button(frame_W_N, text="N", width = 3, font=("Mystery-Day",15), bg="#84161A", fg="#FFE990", command = lambda: [disabled_btn(btnN), programme_moteur() ] )
btnN.pack(side= LEFT)









# ------------------------- CopyLeft ------------------------
copyLeft = Label(fen,
                font=("Mystery-Day",7),
                text= f"   CopyLeft:Greta78/ABDERRAHIM/JARFAR/SAMIA/SIKOU/WAHIB - Sounds:hell/crim/blade/shirojyuu/jincheng {+150*' '}",
                bg="black",
                fg="#FFE990",
                height=2)

copyLeft.place( x=0, y=691)





# ------------------------- FIN ------------------------
fen.mainloop()

print( "*** FIN DE L'APPLICATION PENDU ***" )



# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU

# MANQUE L'AFFICHAGE DU MOT SI ON A PERDU











