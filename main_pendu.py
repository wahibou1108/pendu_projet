#coding:utf-8
# fichier main_pendu.py

'''
ZONE DE TEST FONCTION ENTRE LES LIGNES 15 ET 40 :
-------------------------------------------------
MAIS PENSER A LES INTEGRER PAR LA SUITE A VOS MODULE RESPECTIFS
ET LES IMPORTER VIA LA NOTATION POINTEE COMME DANS L'EXEMPLE :
https://docs.google.com/drawings/d/11fcRO11Jpc06jaaqctlZfIPX_ASjFkrGnvvL_YCMnEU/edit
CECI AFIN DE GARDER UN CODE AUSSI LISIBLE QUE POSSIBLE
'''



























# ------------------------ LIGNE 40 ----------------------
# -------- J'IMPORTE CHAQUE MODULE DE MA SCRUM -----------

import module_samia as ms
import module_abder as ma
import module_wahib as mw
import module_jarfar as mj
import module_sikou as mk


# ------------------ J'IMPORTE TKINTER -------------------

import tkinter as tk

# ------------------------- DÉBUT ------------------------
# ----------------- TKINTER COMMENCE ICI -----------------

racine = tk.Tk()
racine.title("Jeux du pendu sur Tkinter")
racine.iconbitmap("src/IcoPendu9.ico")
racine.geometry("800x600")
racine.resizable(width=False, height=False)    # Pour interdire le redimentionnement en largeur ou en hauteur


#racine.positionfrom("user")
#racine.sizefrom("user")
#racine.geometry("800x600+300+300")







































# ------------------------- FIN ------------------------
racine.mainloop()














