# fichier module_samia.py





import random
from unidecode import unidecode

#j'utilise unidecode et sa fonction du meme nom qui retourne une chaine 
# de caractere sans accent. Pour l'utiliser il faut l'installer au prealable

#la fonction guessWord demande a l'utilisateur de choisir une categ et en fonction du choix entré, 
#la fonction parcourt le fichier approprié et retourne un mot au hasard de la liste grace a la fonction random et sa methode choice

def guessWord():
    categorie =input("choisissez une categorie : animaux, sports, villes, fruits et legumes : ")
    if categorie == "animaux" :
        filename='animals.csv'
        with open(filename, 'r', encoding='utf-8') as f:  
            line = f.readlines()
            word = (unidecode(random.choice(line).upper()))
            print(word)
        
        #print(unidecode(random.choice(line).upper()))

    elif categorie == "sports" :
        filename ="sports.csv"
        print(filename)
    elif categorie == "fruits et legumes"  :
        filename ='fruitslegumes.csv'
        print(filename)
    elif categorie == "villes"  :
        filename ='villes.csv'
        with open(filename, 'r', encoding='utf-8') as f:  
            line = f.readlines()
            word = (unidecode(random.choice(line).upper()))
    return word

 #la fonction hideWord remplace chaque caractere d'un mot donné par des tirets et vise versa et retourne le mot on met le -1 car le dernier caractere est un espace
    
def hideWord(mot , listWord=[]):
    #caract='_ '*len(mot)
    caract=' '
    for i in mot:
        if i in listWord:
            caract += i + ' '
        else:
            caract += '_'    

    return caract[:-1]
#fonction qui demande a l'utilisateur de saisir une lettre, verifie que c'est une lettre et non un autre caractere et la retourne en majuscule
def saisieLettre():
    lettre=input("veuillez entrez une lettre svp : ")
    if len(lettre)>1 or ord(lettre)<65 or ord(lettre)>122:
        return saisieLettre()
    else:
        return lettre.upper()

#fonction qui initialise un jeu  
def init_jeu():
    global partie_en_cours, nb_erreurs, mot_a_deviner, show
    partie_en_cours = True 
    nb_erreurs = 0  
    mot_a_deviner = guessWord()
    show = hideWord(mot_a_deviner)

#global partie_en_cours, nb_erreurs
init_jeu()#on initialise le jeu
if partie_en_cours:
    print('Le mot à deviner est : ' , show)
    lettres_saisies=[]
    while '_' in show and nb_erreurs<9:
        lettre=saisieLettre()
        if lettre not in lettres_saisies:
            lettres_saisies+=[lettre]
        if lettre not in mot_a_deviner:
            nb_erreurs+=1
        show=hideWord(mot_a_deviner, lettres_saisies)
        print('\n Le mot a deviner : ', show , ' '*2, 'nb d\'erreurs restant:',9 - nb_erreurs)





if __name__ == "__main__":

    # FAIRE MES TESTS ICI
    pass


