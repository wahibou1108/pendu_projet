#***********************************************
#  Jeu du Pendu réalisé en PYTHON via Tkinter  *
#            sous environement Window          *
#           avec la collaboration de :         *
#      Samia Abderrahim Jarfar Sikou Wahib     *
#***********************************************


# LE FICHIER PRINCIPAL A EXECUTER EST LE SUIVANT ---->  main_pendu.pyw

python main_pendu.pyw		---> POUR EXECUTER LE FICHIER EN LIGNE DE COMMANDE SOUS WINDOWS
python3 main_pendu.pyw		---> POUR EXECUTER LE FICHIER EN LIGNE DE COMMANDE SOUS MAC




# Pour éviter les bugg suivre les quelques consignes ci-dessous :
#---------------------------------------------------------------

pip install pygame	   ------> pour le son

pip install unidecode	   ------> pour oter les accents trémas oe etc



Installer cette police via le lien, sinon elle se trouve également dans le dossier src : 
---------------------------------------------------------------------------------------

https://www.dafont.com/fr/mystery-day.font?fpp=200&text=Bienvenue+dans+le+jeux+du+pendu+%21



Le dossier /src est à coller à la racine du projet :
---------------------------------------------------

Il contient les sons, la police, les images, les fichiers.csv contenant les mots

Ce dossier /src SERA accessible via le lien gDrive que j'afficherai ci-dessous :

######################################
#				     #
#      lien dossier src/ à venir     #
#				     #
######################################





################################################################
#         VOICI LA LISTE DES SITES QUI NOUS ONT AIDÉ           #
#        DANS LA RÉALISATION DE CE PENDU (FILE ROUGE)*         #
# LA PARTIE GRAPHIQUE EST FAITE ENTIEREMENT SOUS ILLUSTRATOR   #
#            LES SONS SONT RETOUCHÉS VIA AUDACITY	       #
################################################################
*LISTE NON EXAUSTIVE



PETITE PRECISION CE PROGRAMME N'UTILISE PAS :

- les event avec bind()
- PIL de la bibliotheque pillow
- textvariable avec StringVar()


VOICI LA LISTE DES SITES QUI ON PERMIT DE RÉALISER CE PENDU :
------------------------------------------------------------

https://waytolearnx.com/2020/06/interface-graphique-avec-tkinter-python.html

https://python.sdv.univ-paris-diderot.fr/20_tkinter/

https://s15847115.domainepardefaut.fr/python/tkinter/fenetre_disposition_pack.html

https://www.delftstack.com/fr/tutorial/tkinter-tutorial/tkinter-message-box/

https://www.pythontutorial.net/tkinter/tkinter-messagebox/

https://www.pythontutorial.net/tkinter/tkinter-pack/

https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_grid.wp

https://stackoverflow.com/questions/41655618/restart-program-tkinter  --> Comment reset un programme via os




LIENS YT :
---------

https://youtu.be/OdA0kJPrMYQ

https://youtu.be/H0BFsl2_St4?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://www.youtube.com/channel/UCOmaIY1XOb8K2-nLh9OGAdg

https://youtu.be/V-VJLcvqfTA?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/JdSqSKrPhSw?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/HEfks_qSZRo?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/5DAXmvCGbLw?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/V-VJLcvqfTA	  --> Pour arreter le son à la fermeture de la window via la croix








#********** A FAIRE *********

La liste des différentes fonctionnalités à penser et à se dispatcher :
---------------------------------------------------------------------

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








