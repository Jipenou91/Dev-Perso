import random


def selection_ordi():
    choix_ordi = random.randint(1,3)

    if choix_ordi == 1:
        return "pierre"
    elif choix_ordi == 2:
        return "papier"
    else:
        return "ciseau"
    
def resultat(choix_user, trad_choix_ordi):
    if choix_user == "pierre":
        if trad_choix_ordi == "pierre":
            return "egalite"
        elif trad_choix_ordi == "papier":
            return "perdu"
        else:
            return "gagne"
        
    elif choix_user == "papier":
        if trad_choix_ordi == "pierre":
            return "gagne"
        elif trad_choix_ordi == "papier":
            return "egalite"
        else:
            return "perdu"
        
    else:
        if trad_choix_ordi == "pierre":
            return "perdu"
        elif trad_choix_ordi == "papier":
            return "gagne"
        else:
            return "egalite"
        
def choix():
    choix_valides = ["pierre", "papier", "ciseau"]
    choix_user = ""
    while choix_user not in choix_valides:
        choix_user = input("Choisissez entre pierre, papier, ciseau: ").lower()
        if choix_user not in choix_valides:
            print("Choix invalide, veuillez reessayer.")
    print("Votre choix est : ", choix_user)
    print()
    return choix_user

def choix_pc():
    choix_ordi = selection_ordi()    
    print("Le choix de l'ordi est : ", choix_ordi)
    return choix_ordi

def jeu(score, score_ordi):
    print("Bienvenue dans 1 2 3 pierre feuille ciseau \n")
    choix_user = choix()
    choix_ordi = choix_pc()
    resultat_final = resultat(choix_user, choix_ordi)

    if resultat_final == "gagne":
        print("Vous avez gagne!!")
        score+=1
        
    elif resultat_final == "perdu":
        print("Vous avez perdu")
        score_ordi+=1
    else:
        print("egalite, on recommence")
        jeu(score, score_ordi)
     
    print()
    
    print("Score:   utilisateur = ",score, "/ ordi = ",score_ordi)
    
    print()
    
    choix_relance = ""
    choix_valides = ["oui", "non"]
    while choix_relance not in choix_valides:
        choix_relance = input("Voulez vous relancer une partie (oui/non) : ").lower()
        if choix_relance not in choix_valides:
            print("Choix invalide, veuillez reessayer.")
    if choix_relance == "oui":
        print()
        print()
        print()
        jeu(score, score_ordi)
    else:
        print("Au revoir")

jeu(0,0)
            
    
        
    