# fichier module_wahib.py

import webbrowser
#from math import *


def wikiHelp():
    return webbrowser.open_new("https://fr.wikipedia.org/wiki/Le_Pendu_(jeu)")









if __name__ == "__main__":

    '''
    FAIRE MES TESTS ICI

    replace
    find
    join
    insert

    '''

    mot = "MARRON"

    mot_masque = [ "_" for i in range(len(mot))]

    mot_masque = " ".join(mot_masque)

    print(mot_masque)


    '''
    for i in range(len(mot)):
        print(" _ ")

    lettre = input("Entrez une lettre :")

    if i == mot[0]:
        print("Bravo !")
    else:
        print("Faux")

    '''

    m = len(mot)
    for i in mot:
        m = mot.replace(i,"-")
    print(mot)
    print(m)


    print("----------------")






