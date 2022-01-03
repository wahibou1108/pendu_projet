#coding:utf-8
import module_wahib as mw       #
from tkinter import *           # Pour l'interface graphique GUI
from tkinter import messagebox  # POUR L'affichage des popup windows
import pygame                   # J'importe pygame pour gérer le son en boucle
import random                   # POUR CHOISIR UN MOT DANS UNE LISTE VIA CHOICE()







# ------------- INITIALISATION TK - TITRE - ET REDIMENTIONNEMENT FENETRE  -------------

fen = Tk()                      # INITIALISATION DE TKINTER
pygame.mixer.init()             # INITIALISATION DE PYGAME


fen.title("Jeux du pendu sur TKinter")
#fen.resizable(width=False, height=False)  # Empeche le redimentionnement L x H fixé à 800 x 600
#fen.iconbitmap("src/IcoPendu9.ico")      # ATTENTION CETTE LIGNE CASSE LE CENTRAGE DE LA GUI DANS L'ECRAN







# ------------- CENTRER LA FENETRE PRINCIPALE TKINTER AU MILIEU DE L'ECRAN  -------------

largeur_ecran = int(fen.winfo_screenwidth())
hauteur_ecran = int(fen.winfo_screenheight())
largeur_fenetre = 798
hauteur_fenetre = 670

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

# ECRITURE .FORMAT
#geo = "{}x{}+{}+{}".format(largeur_fenetre,  hauteur_fenetre,  posX,  posY)

# ECRITURE PLUS LISIBLE
geo = f"{largeur_fenetre}x{hauteur_fenetre}+{posX}+{posY}"

fen.geometry(geo)














# CE MINI PENDU COMMENCE SIMPLE AVEC 3 LETTRES/BOUTON ET 4 MOTS ALEATOIRES
# C'EST L'APPUIS SUR LE CLAVIER QUI REMPLACE LE INPUT EN CONSOLE
# -------------------------- DEBUT ALGORITHME PENDU -----------------------------

print("--- DÉBUT DE L'ALGORITHME PENDU ---")





fruits          = ["abb","acc","bbc","aabbcc"]

aleatoire       = random.choice( fruits ).upper()

#perime          = [] # CETTE LISTE VA SE REMPLIR DE BONNES ET DE MAUVAISES LETTRE POUR GRISER LES TOUCHES ENSUITE

bravo = ["_"] * len( aleatoire ) # ICI J'AFFCIHE AUTANT D'UNDERSCORE QU4IL Y A DE LETTRE MOT RANDOME

print("DEBUG :",aleatoire)






# ----- FRAME PRINCIPAL DE CHAQUE ELEMENT CI-DESSOUS ------

framePendu = Frame(fen)
framePendu.pack(pady = 20)





# ----- IMAGE ------

canvImg = Canvas( framePendu, width=100, height = 100, bg = "orange" )

if True:

    img = PhotoImage(file=f"src/_divers/pendu_picto{9}.png")
    canvImg.create_image(0, 0, anchor=NW, image = img)  # 50, 50 ici font référence au centre de l'image si je retire anchor
    canvImg.pack()







# RELATION BOUTON JOUER ET LABEL ETAPE 3 / 3

# ---- FONCTION AFFICHE RANDOM AVEC UNDERSCORES -----

def label_cacher():
    mot_under.set(" ".join( bravo ))

    # CETTE FONCTION A UNIQUEMENT POUR BUTE D'AFFICHER DANS MON LABEL ...
    # ... LE NOMBRE DE UNDERSCORES QUE RENVOIE BRAVO, AVEC UN ESPACE ENTRE CHAQUE VIA .JOIN()






# RELATION BOUTON JOUER ET LABEL ETAPE 1 / 3

# _ _ _ _ LABEL RANDOM _ _ _ _

mot_under = StringVar() 

mot_under.set("⌐■_■")

labelJoue = Label(framePendu, textvariable = mot_under)
labelJoue.pack()
# mot_under est activé par le bouton joué qui lance une action (voir fonction label_cacher())







# RELATION BOUTON JOUER ET LABEL ETAPE 2 / 3

# ----- BOUTON JOUER QUI AFFICHE LE LABEL _ _ _ _ -------

btnJoue = Button(framePendu, text="JOUER", command = label_cacher )
btnJoue.pack()







# ----- LABEL LEN ( MOT CACHÉ ) JUSTE POUR DÉBUGUER  -------

label_longeur_lettre = Label(framePendu, text=f"DÉBUG : Trouvez un mot '{aleatoire}' \ncontenant '{len(aleatoire)}' lettres")
label_longeur_lettre.pack()







# ----- FONCTION DESACTIVANT LE CLIC SUR UNE LETTRE APRES APPUIS -------

def disabled_algo_pendu(btn):


    clic_lettre = btn['text'].upper()   # JE STOCK LA LETTRE CHOISIE ET EN MAJUSCULE

    print("DEBUG : ",clic_lettre)

    if btn['state'] == NORMAL:          # POUR GRISER LES TOUCHES
        btn['state'] = DISABLED



    # COMMENCEMENT DE L'ALGO PENDU
    #------------------------------
    
    c = 0

    jouer = True

    while jouer :

        c += 1

        if clic_lettre in aleatoire:        # DEBUT DE L'ALGO PENDU
            print(f"DEBUG : YES '{clic_lettre}' est dans aleatoire")

            index = 0

            for j in aleatoire:

                if j == clic_lettre:
                    bravo[index] = clic_lettre

                    label_cacher()          # APPELLE DE MA FONCTION PLUS HAUT POUR AFFICHER LES LETTRE MASQUEES

                #if btn['text'] not in aleatoire:

                index = index + 1



        else:
            print(f"DEBUG : NO '{clic_lettre}' n'est pas dans aleatoire")
                                            # ICI L'IMAGE DU PENDU 1 PUIS L'IMAGE 2 PUIS 3 ETC





        if '_' not in bravo:
            print(f"GAGNÉ ! Gagné en '{c}' coups")
            print("-->",bravo)
            jouer = False
            break


        if c > 3:
            print(f"PERDU ! Joué en '{c}' coups")
            jouer = False





# FRAMECLAVIER EST UNE SOUS FRAME DE FRAMEPENDU QUI EST UNE SOUS FRAME DE FEN DE TK()

frameClavier = Frame(framePendu)
frameClavier.pack(pady = 20) # fill='x'

# LA FONCTION ANONYME LAMBDA ET UNE SOLUTION QUI PERMET DE PASSER UN PARAMETRE A SA PROPRE FONCTION
# CAR COMMAND EST EGALE UNIQUEMENT A DES FONCTION SANS PARAMETRE. LAMBDA CONTRE CE PROBLEME

btnA = Button(frameClavier, text="A", command = lambda: disabled_algo_pendu(btnA) )
btnA.pack(side= LEFT)

btnB = Button(frameClavier, text="B", command = lambda: disabled_algo_pendu(btnB) )
btnB.pack(side= LEFT)

btnC = Button(frameClavier, text="C", command = lambda: disabled_algo_pendu(btnC) )
btnC.pack(side= LEFT)







# LABEL RESTE A FAIRE

resteAfaire = Message(framePendu,
                    width = 200,
                    relief=RAISED,
                    justify = 'left',
                    text="TRAVAIL DE GROUPE \n\n\
PROCHAINS DEFIS : \n(LISTE A METTRE A JOUR)\n\
- Faire défiler les images à chaque coups perdus \n\
- Le bouton 'jouer' doit pouvoir stoper une partie en cours avec un message d'alerte\n\
- Afficher un label 'BRAVO !' si je gagne + sound bravo (voir /src)\n\
- Afficher un label 'PERDU, CLIQUEZ SUR JOUER' + sound cri (voir /src)\n\n\
APRES LES TACHES CI-DESSUS :\n\
- RELIER LE PENDU A UN FICHIER .CSV \n\
- AFFICHER LE RESTE DES BOUTONS CLAVIER\n\n\
- EN DERNIER INTEGRER LA VRAI PARTIE GRAPHIQUE etc.")

resteAfaire.pack()



























# ------------------------- FIN ------------------------
fen.mainloop()

print( "*** FIN DE L'APPLICATION PENDU ***" )

