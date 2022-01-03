#************************************
Pendu réalisé en PYTHON             *
avec la collaboration de :          *
Samia Abderrahim Jarfar Sikou Wahib *
#************************************

Pour éviter les bugg :

pip install pygame	# pour le son
pip install unidecode	# pour oter les accents trémas oe etc

POLICE IDENTIQUE DANS TOUT LE JEUX A INSTALLER SUR SON ORDI :
------------------------------------------------------------
https://www.dafont.com/fr/mystery-day.font?fpp=200&text=Bienvenue+dans+le+jeux+du+pendu+%21

#****************************
Le dossier /src est à coller à la racine de votre projet 
Il contient les sons les image et les fichiers.csv

Ce dossier /src sera accessible via le lien gDrive que j'afficherai ci-dessous :
---  lien à venir ---


#****************************
La liste des différentes fonctionnalités 
à penser et à se dispatcher :
-----------------------------------------

-> Trouver la bibliothèque python contenant des catégories de mots rassemblées en Clé Valeur


1- Redaction des fichiers contenant des listes de mots par catégorie

   - Rédaction de fichiers par niveau de difficulté


2- Décider de gérer le niveau difficulté dans la façon dont on va extraire le mot et l’afficher, 
   dans l’affichage du mot( faire apparaître quelques lettres suivant le niveau de difficulté etc.. )


3- Choix de l’interface(tkinter, pygame etc..)


PARTIE TECHNIQUE

1- fonctionnalité de gestion de fichier et extraction d’un mot au hasard parmi une liste de mots

2- L’afficher en tant que tuple( car c’est le seul typage indexable mais  non modifiable)

3- Affichage du mot extrait sous forme de tiret

4- Gestion et affichage du clavier virtuel ( accorder l’affichage à l’événement clavier(pour chaque lettre))

5- Fonctionnalité qui teste si une lettre est présente dans le mot extrait, 
	
	- nous l’affichons à sa place en remplaçant le tiret en question sinon nous grisons la touche "événement" 

	- et/ou nous l’affichons en dessous du mot ou à part dans un cadre lettres incompatibles(à voir)

6- Fonctionnalité qui a chaque lettre incompatible affiche étape par étape le dessin du pendu

7- Fonctionnalité qui affiche le mot fini puis le status "gagné"

8- Une autre qui affiche le status perdu avec le dessin complet du pendu

9- Affichage des tentatives restantes

