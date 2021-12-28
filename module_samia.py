# fichier module_samia.py





import random
from unidecode import unidecode

#j'utilise unidecode et sa fonction du meme nom qui retourne une chaine 
# de caractere sans accent. Pour l'utiliser il faut l'installer au prealable

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

    
        
def hideWord(mot , listWord=[]):
    #caract='_ '*len(mot)
    caract=' '
    for i in mot:
        if i in listWord:
            caract += i + ' '
        else:
            caract += '_'    

    return caract[:-1]

def saisieLettre():
    lettre=input("veuillez entrez une lettre svp : ")
    if len(lettre)>1 or ord(lettre)<65 or ord(lettre)>122:
        return saisieLettre()
    else:
        return lettre.upper()

  
def init_jeu():
    global partie_en_cours, nb_erreurs, mot_a_deviner, show
    partie_en_cours = True 
    nb_erreurs = 0  
    mot_a_deviner = guessWord()
    show = hideWord(mot_a_deviner)

#global partie_en_cours, nb_erreurs
init_jeu()
if partie_en_cours:
    print('Le mot à deviner est : ' , show)
    lettres_incompatibles=[]
    while '_' in show and nb_erreurs<9:
        lettre=saisieLettre()
        if lettre not in lettres_incompatibles:
            lettres_incompatibles+=[lettre]
        if lettre not in mot_a_deviner:
            nb_erreurs+=1
        show=hideWord(mot_a_deviner, lettres_incompatibles)
        print('\n Le mot a deviner : ', show , ' '*2, 'nb d\'erreurs restant:',9 - nb_erreurs)





if __name__ == "__main__":

    # FAIRE MES TESTS ICI
    pass


