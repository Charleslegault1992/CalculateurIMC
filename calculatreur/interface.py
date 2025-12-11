#Créer un calculateur d'IMC avec différentes fonctionnalités
# Défis Avancés
# Gérer les merge conflicts sur main.py
# Utiliser Git Flow (branches feature/develop/main)
# Faire des rebases pour garder l'historique propre

def demander_infos():
    poids = 0
    while True:
        try:
            if poids == 0:
                poids = int(input("Entrez votre poids (en kg.): "))                
            taille = int(input("Entrez votre taille (en cm.): "))
            return poids, taille
        except ValueError:
            print("Cette entrée est invalide, veuillez entrer seulement des nombres")
    # Demande poids et taille

def afficher_resultat(imc, categorie):
    pass
    # Affiche joliment


demander_infos()
