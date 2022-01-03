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
    messagebox.showinfo("Règles du jeux", "Ce jeux consiste à trouver un mot avec un nombre de tentative limité, Ce jeux consiste à trouver un mot avec un nombre de tentative limité,Ce jeux consiste à trouver un mot avec un nombre de tentative limité")




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

















# ---- ALGORITHME PENDU VIA LE TERMINAL -------  ALGORITHME PENDU VIA LE TERMINAL -------
# ---------------------------------------------------------------------------------------


if __name__ == "__main__":


    fen = Tk()
    fen.geometry("400x200")
    fen.resizable(width=False, height=False)




    # ------------ COMMENCEMENT --------------

    # POUR AFFICHER BRAVO COMME CECI  _   _   _   _   _   _
    def cacher(): # " ".join(bravo) fait la même chose
        for i in bravo:
            print(i, end=" ")



    fruits          = ["marron","banane","pomme"]

    mot_random      = random.choice( fruits )
    print("\n\n DEBUG :",mot_random)

    perime          = [] # CETTE LISTE VA SE REMPLIR DE BONNES ET DE MAUVAISES LETTRE POUR GRISER LES TOUCHES ENSUITE

    bravo           = ["_"] * len( mot_random )



    under_ = " ".join(bravo) # MEME RESULTAT QUE FONCTION CACHER()
    print(f"Le mot '{under_}' contient '{len(mot_random)}' lettres \n")
    #cacher()



    c = 0 # compteur pour afficher les images du pendu à chaque echec

    while True:

        c = c + 1

        devine = input("Entrez une lettre : ")

        if devine in mot_random:

            index = 0

            for j in mot_random:

                if j == devine:
                    bravo[index] = devine                            # JE REMPLACE LES UNDERSCORES PAR LES LETTRES TROUVÉES


                    if devine not in perime:
                        perime.append(devine)                        # POUR STOCKER LA LETTRE DANS LA LISTE
                    else:
                        print(f"BONNE lettre {devine} déjà cliquée") # ICI GRISER LA TOUCHE CLAVIER


                index += 1                                           # J'AJOUTE 1 A CHAQUE TOUR DE FOR POUR AVANCER EN MEME TEMPS QUE J DE FOR


            # --- AFFICHER LE LABEL TKINTER ICI --> M _ R R _ N ---

            cacher()




        else:
            if devine not in perime:
                perime.append(devine)                               # POUR STOCKER LA LETTRE DANS LA LISTE


                             # ICI GRISER LA TOUCHE CLAVIER

                             # ICI IMAGE PENDU N1, PUIS N2, PUIS N3 etc


            else:
                print(f"MAUVAISE lettre {devine} déjà cliquée")

            print("perime ->", perime)




        # --- POUR ARRETER LE WHILE LORSQUE BRAVO N'A PLUS DE UNDERSCORE
        # CAR BRAVO AU DEPART NE POSSEDE QUE DES UNDERSCORES ET SE REMPLI A CHAQUE TOUR DE FOR ---
        #print("Débug :", bravo)

        if '_' not in bravo:
            print("BRAVO !")
            break




        print("Nombre de coups joué :",c)




        # --- POUR ARRETER LE JEUX AU DELA DE 9 ECHECS ---
        if c > 9:
            print("PERDU !")
            break


    # ------------ FIN ALOGO PENDU --------------
    # -------------------------------------------









# ------- TEST ----- TEST ---- TEST ---- TEST ---- TEST ---- TEST --------


    def recup_lettre():
        labA.config( text = btn_lire['text'] )


    ma_frame = Frame(fen)
    ma_frame.pack()


    # 1 - IMAGE -
    canvImg = Canvas( ma_frame, width =100, height = 100, bg = "orange" )
    canvImg.grid(row=0, column = 1)

    img = PhotoImage(file="src/_divers/IcoPendu9.png")#.zoom(1)            # RECUPERATION ET AJOUT IMAGE

    canvImg.create_image(50, 50, image = img)  # 50, 50 ici font référence au centre de l'image si je retire anchor
    #canvImg.create_image(50, 50, image = img, anchor = NW ) # prends les deux valeur et part du coin NW de l'image



    # AFFICHER LE LABEL BRAVO  _   _   _   _   _   _

    def cach():
        txt.set(" ".join(bravo))


    txt = StringVar()
    txt.set("underscore à venir")

    labelBravo = Label( ma_frame, bg="red", textvariable = txt )
    labelBravo.grid(row=1, column = 1)

    btnJouer = Button( ma_frame, text="JOUER", command = cach)
    btnJouer.grid(row=2, column = 1)








    fen.mainloop()

# ------------ FIN --------------

    print("\nTout est OK !")





