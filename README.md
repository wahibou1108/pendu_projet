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



Le dossier /src (lien ci-dessous) est à coller à la racine du projet :
---------------------------------------------------------------------
Il contient les sons, la police, les images, les fichiers.csv contenant les mots.
https://drive.google.com/drive/folders/1A0FYuGtiQVXzD3JTjg74jbxM-Ng9UhXw?usp=sharing










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



SITES WEB QUI ON PERMIT DE RÉALISER CE PENDU :
---------------------------------------------

https://waytolearnx.com/2020/06/interface-graphique-avec-tkinter-python.html

https://python.sdv.univ-paris-diderot.fr/20_tkinter/

https://s15847115.domainepardefaut.fr/python/tkinter/fenetre_disposition_pack.html

https://www.delftstack.com/fr/tutorial/tkinter-tutorial/tkinter-message-box/

https://www.pythontutorial.net/tkinter/tkinter-messagebox/

https://www.pythontutorial.net/tkinter/tkinter-pack/

https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_grid.wp

https://stackoverflow.com/questions/41655618/restart-program-tkinter  --> Comment reset un programme via os



YOUTUBE :
--------

https://youtu.be/OdA0kJPrMYQ

https://youtu.be/H0BFsl2_St4?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://www.youtube.com/channel/UCOmaIY1XOb8K2-nLh9OGAdg

https://youtu.be/V-VJLcvqfTA?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/JdSqSKrPhSw?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/HEfks_qSZRo?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/5DAXmvCGbLw?list=PL3gLNd_-DXPYN2A3f6SRYbyieG9lIUY7d

https://youtu.be/V-VJLcvqfTA	  --> Pour arreter le son à la fermeture de la window via la croix










#********** RESTE A AMELIORER *********

1 OK -         Faire défiler les images à chaque coups perdus

2 OK PRESQUE - Le bouton 'jouer' doit pouvoir stoper une partie en cours avec un message d'alerte, puis relancer la partie

3 OK PRESQUE - Afficher un label 'BRAVO !' si je gagne + music bravo (voir /src)

4 OK PRESQUE - Afficher un label 'PERDU !' si je perds + music perdu (voir /src)

5 -            RELIER LE PENDU A UN FICHIER .CSV contenant plusieur categories liste mot

6 OK -         TESTER LE TOUT AVEC TOUT L'ALPHABET

7 -            CREER 3 NIVEAU DE DIFFICULTE

8 -            AFFICHER LE MOT DANS LE LABEL SI JE PERDS

9 OK -         ENFIN EN DERNIER INTEGRER LE VRAI GRAPHISME










