#coding:utf-8
import module_wahib as mw       #
from tkinter import *           # Pour l'interface graphique GUI
from tkinter import messagebox  # POUR L'affichage des popup windows
import pygame                   # J'importe pygame pour gérer le son en boucle
import random                   # POUR CHOISIR UN MOT DANS UNE LISTE VIA CHOICE()
from unidecode import unidecode # pour remplacer les caracteres avec accents lorsque j'appele une liste de mots via random
import os




# ------------- INITIALISATION TK - TITRE - ET REDIMENTIONNEMENT FENETRE  -------------

fen = Tk()                      # INITIALISATION DE TKINTER
pygame.mixer.init()             # INITIALISATION DE PYGAME


fen.title("Jeux du pendu PROTOTYPE TKINTER")
#fen.resizable(width=False, height=False)  # Empeche le redimentionnement L x H fixé à 800 x 600
#fen.iconbitmap("src/IcoPendu9.ico")      # ATTENTION CETTE LIGNE CASSE LE CENTRAGE DE LA GUI DANS L'ECRAN





# ------------- CENTRER LA FENETRE PRINCIPALE TKINTER AU MILIEU DE L'ECRAN  -------------

largeur_ecran = int(fen.winfo_screenwidth())
hauteur_ecran = int(fen.winfo_screenheight())
largeur_fenetre = 400
hauteur_fenetre = 800

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)
fen.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{posX}+{posY}")




# --- ESSAI SON ---
'''
def son7():
    pygame.mixer.music.load('src/sound_perdu.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)

btnSon = Button(fen, text="btnSon", command = mw.son7)
btnSon.pack()

'''









def restart():
    pygame.quit()                         # CETTE LIGNE EMPECHE LE SON DE CONTINUER APRES LA FERMETURE DE LA FENETRE
    fen.destroy()                         # CETTE LIGNE ARRETE L'APPLICATION
    os.startfile("main_proto_pendu.pyw ")            # CETTE LIGNE RELANCE L'APPLICATION.
                                          # LE .PYW ME PERMET D'EMPCHER L'OUVERTURE DU TERMINAL QUI S4OUVRE SI LE FICHIER EST EN .PY


# ------------------------- MENU DEROULANT HAUT GACHE --------------------------

menu_bar = Menu(fen)

# SOUS ONGLETS DEROULANTS LIES AU  1er LABEL
derouler_1 = Menu(menu_bar, tearoff=0 ) # tearoff=0 m'ote cette barre moche qui s'affiche en haut du menu déroulant
derouler_1.add_command(label="Jouer", command = restart)  # COMMAND A VENIR
derouler_1.add_command(label="Quitter", command= fen.destroy ) #  command= fen.destroy  ////  command = pop_ask_cut_window_et_son

menu_bar.add_cascade(label="Jouer/Quitter", menu = derouler_1, activeforeground = "#84161A")



derouler_2 = Menu(menu_bar, tearoff = 0 )
derouler_2.add_command(label="Facile")          # COMMAND A VENIR
derouler_2.add_command(label="Moyen")           # COMMAND A VENIR
derouler_2.add_command(label="Difficile")       # COMMAND A VENIR

menu_bar.add_cascade(label="Niveaux", menu= derouler_2)


fen.config(menu= menu_bar)

















# -------------------------- DEBUT ALGORITHME PENDU -----------------------------

# CE MINI PENDU COMMENCE SIMPLE AVEC QLQ LETTRES BOUTONS ET QLQ MOTS ALEATOIRES
#  C'EST L'APPUIS SUR LE CLAVIER TKINTER AZERTY QUI REMPLACE LE INPUT EN CONSOLE

# -------------------------------------------------------------------------------

print("\n\n--- DÉBUT DE L'ALGORITHME PENDU ---")




#animaux         = ["aab","aac","bba","bbc","aabbcc","azerty","coq"]

chanteur        = ["chebkhaled","chebmami","zaho","idir","chebhasni","chebbilal","takfarinas","chebnadir","cherifa","chebazahouania","rachidtaha","faudel","algerino","chebnasro"]




aleatoire       = unidecode (random.choice(chanteur).upper() )

print("DEBUG : 'aleatoire' -> :",aleatoire)                 # DEBUG : 'aleatoire' -> : CHEBHASNI




bravo = ["_"] * len( aleatoire )

print("DEBUG : 'bravo' :",bravo)                            # DEBUG : 'bravo' : ['_', '_', '_', '_', '_', '_', '_', '_', '_']



# afficher un compteur

# --------- NIVEAU 1 FACILE CAR DEUX INDICE ET 9 VIES -------------------------- OK LEVEL 1 FACILE PAR DEFAUT

niveau_1_facile = aleatoire[0] + (len(aleatoire)-2)* '_ ' + aleatoire[-1]

print("DEBUG : 'niveau_1_facile' -> :", niveau_1_facile)    # UN indice



'''
li = []
li.extend(aleatoire)
print("je coupe aleatoire -->", li)
print("random.sample -->", random.sample(aleatoire, 2))     # JE VEUX 2 LETTRES DISTINCTES ET NON DEUX LETTRE IDENTIQUES


def f( mot ):

    aleatoire_chaine = []
    aleatoire_chaine.extend( mot )                          # je coupe le mot chaine en liste de lettre

    deux_lettres = random.sample( mot, 2 )                     # je veux extraire 2 lettres distinctes n'importe où dans le mots

    for i in range( len(aleatoire_chaine)):  # 1 2 3 4 5 ...

        for k in range( len(deux_lettres)):  # 1 2

            if aleatoire_chaine[i] == deux_lettres[k]:

                aleatoire_chaine[i] = deux_lettres[k]

    return aleatoire_chaine

print("\nDEBUG fonction f()", f( aleatoire ))
'''


# --------- NIVEAU 2 MOYEN CAR PAS D'INDICE MAIS 7 VIES ------------------------ A FAIRE - PAR EXEMPLE COMMENCER LE PENDU A L'IMAGE 3 ET DESACTIVER LE BOUTON INDICE SI LE CHOIX EST PORTE SUR LE LEVEL 2

niveau_2_moyen = ' '.join(bravo)

print("DEBUG : 'niveau_2_moyen' -> :", niveau_2_moyen)      # PAS d'indice



# --------- NIVEAU 3 DIFFICILE, PAS D'INDICE ET SEULEMENT 5 VIES --------------- A FAIRE - SOIT INCREMENTER L'IMAGE_0 (4 vies) DE 2 SOIT COMMENCER A L'IMAGE_3 (5 vies) ET DESACTIVER L'INDICE








# ---------------------------------------------------------
#                                                          |_________________________
#                                                                                    |
#        FRAME PRINCIPAL DE CHAQUE ELEMENT CI-DESSOUS DISPACHÉS EN GRID()            |
# CETTE FRAME PRINCIPALE INTEGRE D'AUTRES FRAME COMME PAR EXEMPLE UNE FRAME CLAVIER  |
#      AVEC 3 SOUS FRAME, AFIN DE POUVOIR CREER DES BOUTONS ORGANISÉS                |
#         EN GRID() ET NON EN PACK()                        _________________________|
#                                                          |
framePendu = Frame(fen)#                                   |
framePendu.pack(pady = 20)#                                |
#                                                          |
# ---------------------------------------------------------





# ICI AFFICHER LE TITRE DE LA LISTE DE MOT QUE RANDOM.RANDINT CHOISIRA
'''
def f_indice_liste():
    label_indice_liste.config(text = "Chanteur de raï connu")
'''

label_indice_liste = Label(framePendu, text="Chanteur de raï connu".upper())
label_indice_liste.grid( row = 1, column = 0 )










# ------------------ IMAGE DE FOND PERMANANTE ------------------

canvImg = Canvas( framePendu, width=100, height = 100)
img = PhotoImage(file=f"src/pendu_picto{0}.png")
canvImg.create_image(0, 0, anchor=NW, image = img)  # 50, 50 ici font référence au centre de l'image si je retire anchor
canvImg.grid( row = 2, column = 0 )




# ----- IMAGE PAR DESSUS APPELÉ DANS LA BOUCLE ------

def img_label( jusqua9 ):           # LE PARAMETRE ATTEND LE FUTURE COMPTEUR DE 1 à 9

    lab_img = Label(framePendu)
    lab_img.grid( row = 2, column = 0 )
    mon_image = PhotoImage( file = f"src/pendu_picto{jusqua9}.png" )
    lab_img.config(image = mon_image)
    lab_img.image = mon_image





# ETAPE 3 / 3  --->   je crée la fonction liée au bouton "COMMENCER" et au label

def fonc_affiche_mot_cache():                          # CETTE EST APPELÉE DANS LE MOTEUR DU PROGRAMME AFIN DE CONSTAMENT METTRE A JOUR LE LABEL

    labelJoue.configure(text = bravo )




# ETAPE 2 / 3  --->

labelJoue = Label(framePendu, text= bravo, width = 25, height = 2, relief = GROOVE) # J'APPELLE BRAVO MASQUÉ DANS LE LABEL DES LE DÉBUT DE LA PARTIE
labelJoue.grid( row = 3, column = 0 )




#  CODE INUTILE TOUT COMPTE FAIT
'''
def eventSourisG(event):                                # FONCTION EVENT --> EVENEMENT SUR LA SOURIS LORSQUE btnCOMMENCER EST PRESSÉ

    print("DEBUG : presse touche clic gauche")



def fonc_btn_commencer():
    if btnCOMMENCER['state'] == NORMAL:
        btnCOMMENCER['state'] = DISABLED


# ETAPE 1 / 3  --->   je cree mon bouton "COMMENCER"

# ----- BOUTON JOUER QUI AFFICHE DANS LE LABEL (BRAVO) EN FONCTION DU NOMBRE DE LETTRE DANS MOT ALEATOIRE

btnCOMMENCER = Button(framePendu, text="COMMENCER", command = lambda: [ fonc_affiche_mot_cache() , fonc_btn_commencer() ] )                          # ici je dois appeler une fonction qui désactive tout les bouton
btnCOMMENCER.grid( row = 2, column = 0 )

btnCOMMENCER.bind('<Button-1>', eventSourisG)           # EVENEMENT SOURIS CLIC GAUCHE

'''










'''
# ---------- LABEL DEBUG -- A SUPPRIMER -- LABEL DEBUG -- A SUPPRIMER ----------

label_longeur_lettre = Label(framePendu,
                            text=f"DÉBUG - Trouvez le mot : \'{aleatoire}' \n\
contenant '{len(aleatoire)}' lettres {bravo}")
label_longeur_lettre.grid( row = 4, column = 0 )

# ---------- LABEL DEBUG -- A SUPPRIMER -- LABEL DEBUG -- A SUPPRIMER ----------
'''



def f_indice():

    label_longeur_lettre = Label(framePendu, text=f"Indice : '{niveau_1_facile}' \nCe mot contient '{len(aleatoire)}' lettres")
    label_longeur_lettre.grid( row = 4, column = 0 )


btn_indice = Button(framePendu, text="? INDICE ?", command = f_indice)
btn_indice.grid( row = 4, column = 0 )








#                   ALGO PENDU ESSAI n4
# -------------------------------------------------------


def disabled_btn_plus_alogo_pendu(btn): # FONCTION DESACTIVANT LE CLIC SUR UNE LETTRE APRES APPUIS

    global clic_lettre                  # GLOBALE

    clic_lettre = btn['text'].upper()   # JE STOCK LA LETTRE CHOISIE ET EN MAJUSCULE dans la variable clic_lettre

    print(f"\n\nDEBUG : je UPPER() puis DISABLE la touche '{clic_lettre}'")

    if btn['state'] == NORMAL:          # POUR GRISER LES TOUCHES, C'EST CETTE SYNTAXE.
        btn['state'] = DISABLED         # ET LORSQUE JE CLIC SUR UNE TOUCHE, JE LA DISABLE IMMEDITEMENT, AINSI LE PROBLEME EST REGLÉ
                                        # ... CAR ON EST PAS CENSÉ CLIQUER 2 FOIS SUR LA MËME TOUCHE



neuf_coups = 9

quatre_coups = 3

c = 0                                   # GLOBALE

def programme():

    global c
    vrai = True


    while vrai and c <= neuf_coups :


        if clic_lettre not in aleatoire and "".join(bravo) != aleatoire:    # MOTEUR 1 : SI LA LETTRE CLIQUÉ N'EST PAS DANS LE MOT ALEATOIRE ALORS TU NE FAIS RIEN MAIS TU COMPTES A REBOURG

            c = c + 1

            print(f"\nDEBUG MOTEUR_1 : '{clic_lettre}' not in '{aleatoire}'. Compteur ='{c}', plus que '{neuf_coups - c}' tentatives")

            img_label(c)                    # J'APPELLE MA FONCTION IMAGE ET J'AJOUTE UNE NOUVELLE IMAGE PENDU A CHAQUE PERTE

            if c > 5 :
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












'''
#                   ALGO PENDU ESSAI 3
# -------------------------------------------------------
c = 0                                   # ATTENTION VARIABLE GLOBALE

def disabled_btn_plus_alogo_pendu(btn): # FONCTION DESACTIVANT LE CLIC SUR UNE LETTRE APRES APPUIS

    global c

    clic_lettre = btn['text'].upper()   # JE STOCK LA LETTRE CHOISIE ET EN MAJUSCULE dans la variable clic_lettre

    print(f"\n\nDEBUG : je UPPER() puis DISABLE la touche '{clic_lettre}'. Compteur = '{c}'")


    vrai = True

    while vrai and c < 10 :

        if btn['state'] == NORMAL:          # POUR GRISER LES TOUCHES, C'EST CETTE SYNTAXE.
            btn['state'] = DISABLED         # ET LORSQUE JE CLIC SUR UNE TOUCHE, JE LA DISABLE IMMEDITEMENT, AINSI LE PROBLEME EST REGLÉ
                                            # ... CAR ON EST PAS CENSÉ CLIQUER 2 FOIS SUR LA MËME TOUCHE


        if clic_lettre not in aleatoire:    # MOTEUR 1 : SI LA LETTRE CLIQUÉ N'EST PAS DANS LE MOT ALEATOIR ALORS TU NE FAIS RIEN MAIS TU COMPTES A REBOURG

            c = c + 1

            print(f"\nDEBUG MOTEUR_1 : '{clic_lettre}' not in '{aleatoire}'. Compteur ='{c}', plus que '{abs(c-9)}' tentatives")

            img_label(c)                    # J'APPELLE MA FOCNTION IMAGE ET J'AJOUTE UNE NOUVELLE IMAGE PENDU A CHAQUE PERTE
            vrai = False


        elif clic_lettre in aleatoire:      # MOTEUR 2 : SI LA LETTRE CLIQUÉ EST DANS LE MOT ALEATOIR ALORS ...

            print(f"\nDEBUG MOTEUR_2 : '{clic_lettre}' in '{aleatoire}'")

            index = 0                       # INDEX QUI VA SERVIR A TRANSFORMER LES UNDERSCORES EN LETTRE AUTANT QU'IL Y A DE LETTRE CLIQUÉES

            for j in aleatoire:

                if j == clic_lettre:

                    bravo[index] = clic_lettre

                    print(f"  DEBUG FOR / IF : bravo[index] m'affiche '{bravo[index]}' , \
J'avance à la position '{index}' dans le mot:'{aleatoire}'. Compteur ='{c}'")

                    fonc_affiche_mot_cache()    # J'AFFICHE LE LABEL A CHAQUE MODIFICATION

                index = index + 1

            print(f'\nDEBUG : le mot:{"".join(bravo)} correspond il au mot:{aleatoire} ??')


            if "".join(bravo) == aleatoire:
                print(f'\nDEBUG : GAGNÉ GAGNÉ!! le mot:{"".join(bravo)} correspond au mot:{aleatoire}. Compteur = {c}')


            if c == 9:
                print(f"\nDEBUG : PERDU PERDU !! Compteur = '{c}'")

            vrai = False

    print(f"DEBUG FIN FONCTION_PENDU : Compteur = '{c}'")
'''





'''
    #             ALGO PENDU ESSAI 2
    # ----------------------------------------
    #    A CONSERVER POUR LES COMMENTAIRES   |
    # ----------------------------------------
    #       COMMENCEMENT DE L'ALGO PENDU     |
    # ----------------------------------------
    # ----------------------------------------

    c = 0
    vrai = True
    while vrai :

        c += 1

        if clic_lettre in aleatoire:
            print(f"\nDEBUG 1er if : '{clic_lettre}' est dans '{aleatoire}'")

            index = 0

            for j in aleatoire:

                if j == clic_lettre:

                    bravo[index] = clic_lettre

                    print(f"DEBUG if de for : bravo[index]->'{bravo[index]}' , compteur->'{c}'")

                    fonc_affiche_mot_cache()

                index = index + 1

            print(f"DEBUG dans if : '{c}'")


        elif clic_lettre not in aleatoire:

            print(f"\nDEBUG : Il n'y a pas de lettre '{clic_lettre}' dans '{aleatoire}'")
            print(f"DEBUG : premier elif en cours '{c}'")


        elif bravo == aleatoire:

            print(f"\nDEBUG : 2eme elif '{c}'")
            print(f"GAGNÉ en '{c}' coups")
            break

        elif c == 3:

            print(f"\nDEBUG : 3e elif en '{c}' coups")
            print(f"PERDU en '{c}' coups")

        vrai = False
'''





'''
    #           ALGO PENDU ESSAI 1
    # ----------------------------------------
    #    A CONSERVER POUR LES COMMENTAIRES   |
    # ----------------------------------------
    #       COMMENCEMENT DE L'ALGO PENDU     |
    # ----------------------------------------

    def disabled_algo_pendu(btn):

    # ----- FONCTION DESACTIVANT LE CLIC SUR UNE LETTRE APRES APPUIS -------

    global clic_lettre

    clic_lettre = btn['text'].upper()   # JE STOCK LA LETTRE CHOISIE ET EN MAJUSCULE dans la variable clic_lettre

    print("\nDEBUG 1er dans fonction pour DISABLE 'clique_lettre' : ",clic_lettre)

    if btn['state'] == NORMAL:          # POUR GRISER LES TOUCHES, C'EST CETTE SYNTAXE.
        btn['state'] = DISABLED         # ET LORSQUE JE CLIC SUR UNE TOUCHE, JE LA DISABLE IMMEDITEMENT, AINSI LE PROBLEME EST REGLÉ
                                        # ... CAR ON EST PAS CENSÉ CLIQUER 2 FOIS SUR LA MËME TOUCHE

    c = 0                                       # MON COMPTEUR QUI VA ME SERVIR POUR AFFICHER LES IMAGES ET ARRETER LE SCRIPT
    jouer = True
    while jouer :
        c += 1
        if clic_lettre in aleatoire:            # si la lettre cliqué est dans la variable "aleatoire" qui stocke un random.choice, alors j'entre dans le if, ALORS ...
            print(f"DEBUG : YES '{clic_lettre}' est dans {aleatoire}")

            index = 0                           # C'EST INDEX QUI VA PARCOURIR TOUTES LES LETTRES IDENTIQUES DE ALEATOIRE CAR IL AVANCE EN MEME TEMPS QUE J

            for j in aleatoire:                 # J VA RENVOYER CHAQUE LETTRE DU MOT ALEATOIRE

                if j == clic_lettre:            # SI UNE LETTRE DE ALEATOIRE EST EGALE A LA TOUCHE CLAVIER CLIQUÉ ALORS ...

                    bravo[index] = clic_lettre  # ... ALORS BRAVO QUI CONTIENT LE UNDERSCORS VA RECEVOIR DANS BRAVO DE 0 OU DE 1 OU DE N, LA LETTRE CLIQUÉ AUTANT QU'IL Y A DE LETTRE IDENTIQUES

                    print(f"DEBUG bravo[index] : compteur : '{c}' : '{bravo[index]}'")

                    fonc_affiche_mot_cache()              # JE LANCE MA FONCTION fonc_affiche_mot_cache POUR AFFICHER LES LETTRE MASQUEES ET LES DEMASQUER TANT QU'IL Y A DE LETTRE TROUVÉES

                #if btn['text'] not in aleatoire:

                index = index + 1               # J'INCREMENTE INDEX POUR QUE BRAVO [ DE INDEX ] REVOIVE AUTANT DE CLIQUE_LETTRE QUE DE LETTRE QU'IL POSSEDE

            print(f"DEBUG compteur : '{c}' coups")

            if '_' not in bravo:
                print(f"GAGNÉ ! Gagné en '{c}' coups")
                print("-->",bravo)
                break

        else:
            print(f"COMPTEUR : '{c}' coups")
            print(f"DEBUG : NO '{clic_lettre}' n'est pas dans {aleatoire}, NOUVELLE IMAGE PENDU")

        if c > 3:
            print(f"PERDU ! Joué en '{c}' coups")
            jouer = False  # --------------- A REVOIR ------------------
'''





#----------------------------------------------------
#                                                    |
#  FRAMECLAVIER  EST UNE SOUS FRAME DE  FRAMEPENDU   |
#       QUI EST UNE SOUS FRAME DE FEN DE TK()        |
#                                                    |
frameClavier = Frame(framePendu)#                    |
frameClavier.grid( row = 5, column = 0 )#            |
#frameClavier.pack(pady = 20)#                       |
#                                                    |
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



# ------------------------------------- MES BOUTONS DE TEST ------------------------------------
'''
btnA = Button(frame_A_P, text="A", command = lambda: [ disabled_btn_plus_alogo_pendu(btnA), programme() ])
btnA.pack(side= LEFT)

btnB = Button(frame_A_P, text="B", command = lambda: [ disabled_btn_plus_alogo_pendu(btnB), programme() ])
btnB.pack(side= LEFT)

btnC = Button(frame_A_P, text="C", command = lambda: [ disabled_btn_plus_alogo_pendu(btnC), programme() ])
btnC.pack(side= LEFT)

btnD = Button(frame_A_P, text="D", command = lambda: [ disabled_btn_plus_alogo_pendu(btnD), programme() ])
btnD.pack(side= LEFT)

btnE = Button(frame_A_P, text="E", command = lambda: [ disabled_btn_plus_alogo_pendu(btnE), programme() ])
btnE.pack(side= LEFT)

btnF = Button(frame_A_P, text="F", command = lambda: [ disabled_btn_plus_alogo_pendu(btnF), programme() ])
btnF.pack(side= LEFT)

btnG = Button(frame_A_P, text="G", command = lambda: [ disabled_btn_plus_alogo_pendu(btnG), programme() ])
btnG.pack(side= LEFT)
'''



btnA = Button(frame_A_P, text="A", command = lambda: [disabled_btn_plus_alogo_pendu(btnA), programme() ] )
btnA.pack(side= LEFT)

btnZ = Button(frame_A_P, text="Z", command = lambda: [disabled_btn_plus_alogo_pendu(btnZ), programme() ] )
btnZ.pack(side= LEFT)

btnE = Button(frame_A_P, text="E", command = lambda: [disabled_btn_plus_alogo_pendu(btnE), programme() ] )
btnE.pack(side= LEFT)

btnR = Button(frame_A_P, text="R", command = lambda: [disabled_btn_plus_alogo_pendu(btnR), programme() ] )
btnR.pack(side= LEFT)

btnT = Button(frame_A_P, text="T", command = lambda: [disabled_btn_plus_alogo_pendu(btnT), programme() ] )
btnT.pack(side= LEFT)

btnY = Button(frame_A_P, text="Y", command = lambda: [disabled_btn_plus_alogo_pendu(btnY), programme() ] )
btnY.pack(side= LEFT)

btnU = Button(frame_A_P, text="U", command = lambda: [disabled_btn_plus_alogo_pendu(btnU), programme() ] )
btnU.pack(side= LEFT)

btnI = Button(frame_A_P, text="I", command = lambda: [disabled_btn_plus_alogo_pendu(btnI), programme() ] )
btnI.pack(side= LEFT)

btnO = Button(frame_A_P, text="O", command = lambda: [disabled_btn_plus_alogo_pendu(btnO), programme() ] )
btnO.pack(side= LEFT)

btnP = Button(frame_A_P, text="P", command = lambda: [disabled_btn_plus_alogo_pendu(btnP), programme() ] )
btnP.pack(side= LEFT)



btnQ = Button(frame_Q_M, text="Q", command = lambda: [disabled_btn_plus_alogo_pendu(btnQ), programme() ] )
btnQ.pack(side= LEFT)

btnS = Button(frame_Q_M, text="S", command = lambda: [disabled_btn_plus_alogo_pendu(btnS), programme() ] )
btnS.pack(side= LEFT)

btnD = Button(frame_Q_M, text="D", command = lambda: [disabled_btn_plus_alogo_pendu(btnD), programme() ] )
btnD.pack(side= LEFT)

btnF = Button(frame_Q_M, text="F", command = lambda: [disabled_btn_plus_alogo_pendu(btnF), programme() ] )
btnF.pack(side= LEFT)

btnG = Button(frame_Q_M, text="G", command = lambda: [disabled_btn_plus_alogo_pendu(btnG), programme() ] )
btnG.pack(side= LEFT)

btnH = Button(frame_Q_M, text="H", command = lambda: [disabled_btn_plus_alogo_pendu(btnH), programme() ] )
btnH.pack(side= LEFT)

btnJ = Button(frame_Q_M, text="J", command = lambda: [disabled_btn_plus_alogo_pendu(btnJ), programme() ] )
btnJ.pack(side= LEFT)

btnK = Button(frame_Q_M, text="K", command = lambda: [disabled_btn_plus_alogo_pendu(btnK), programme() ] )
btnK.pack(side= LEFT)

btnL = Button(frame_Q_M, text="L", command = lambda: [disabled_btn_plus_alogo_pendu(btnL), programme() ] )
btnL.pack(side= LEFT)

btnM = Button(frame_Q_M, text="M", command = lambda: [disabled_btn_plus_alogo_pendu(btnM), programme() ] )
btnM.pack(side= LEFT)



btnW = Button(frame_W_N, text="W", command = lambda: [disabled_btn_plus_alogo_pendu(btnW), programme() ] )
btnW.pack(side= LEFT)

btnX = Button(frame_W_N, text="X", command = lambda: [disabled_btn_plus_alogo_pendu(btnX), programme() ] )
btnX.pack(side= LEFT)

btnC = Button(frame_W_N, text="C", command = lambda: [disabled_btn_plus_alogo_pendu(btnC), programme() ] )
btnC.pack(side= LEFT)

btnV = Button(frame_W_N, text="V", command = lambda: [disabled_btn_plus_alogo_pendu(btnV), programme() ] )
btnV.pack(side= LEFT)

btnB = Button(frame_W_N, text="B", command = lambda: [disabled_btn_plus_alogo_pendu(btnB), programme() ] )
btnB.pack(side= LEFT)

btnN = Button(frame_W_N, text="N", command = lambda: [disabled_btn_plus_alogo_pendu(btnN), programme() ] )
btnN.pack(side= LEFT)





# NOUVELLE TENTATIVE DE REALISER UN CLAVIER / ECHEC CAR LE SEULE BOUTON RECONNU EST LE Z
'''
a__z = string.ascii_uppercase

print('DEBUG a__z :',a__z)

for i in range(len(a__z)):
    mes_boutons = Button(frameClavier, text=a__z[i], command = lambda: disabled_btn_plus_alogo_pendu(mes_boutons) )
    mes_boutons.pack(side= LEFT)
'''





# MESSAGE RESTE A FAIRE

resteAfaire = Message(framePendu,
                    width = 200,
                    relief=RAISED,
                    justify = 'center',
                    text="TRAVAIL DE GROUPE - PROCHAINS DEFIS DANS CET ORDRE :\n\n\
OK 1- Faire défiler les images à chaque coups perdus \n\n\
OK PRESQUE 2- Le bouton 'jouer' doit pouvoir stoper une partie en cours avec un message d'alerte, puis relancer la partie\n\n\
OK PRESQUE 3- Afficher un label 'BRAVO !' si je gagne + music bravo (voir /src)\n\n\
OK PRESQUE 4- Afficher un label 'PERDU !' si je perds + music perdu (voir /src)\n\n\
5- RELIER LE PENDU A UN FICHIER .CSV contenant plusieur categories liste mot\n\n\
OK 6- TESTER LE TOUT AVEC TOUT L'ALPHABET\n\n\
7- CREER 3 NIVEAU DE DIFFICULTE\n\n\
8- ENFIN EN DERNIER INTEGRER LE VRAI GRAPHISME\n\n\
__FIN__")

resteAfaire.grid( row = 6, column = 0 )













print("\n\n---------- PRINT / DEBUGS / TESTS CONSOLE -----------")















# ------------------------- FIN ------------------------
fen.mainloop()

print( "*** FIN DE L'APPLICATION PENDU ***" )

