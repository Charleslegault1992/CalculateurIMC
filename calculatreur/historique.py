#Créer un calculateur d'IMC avec différentes fonctionnalités
# Défis Avancés
# Gérer les merge conflicts sur main.py
# Utiliser Git Flow (branches feature/develop/main)
# Faire des rebases pour garder l'historique propre

def sauvegarder_calcul(nom, imc):
    # Sauvegarde dans un fichier
    # cree un fichier et ajout les informations dans ce fichier
    with open("imc_historique.txt", "r", encoding="utf-8") as fichier:
        fichier.write(f"{nom}: {imc}\n")

def afficher_historique():
    # Lit le fichier
    try:
        with open("imc_historique.txt", "r", encoding="utf-8") as fichier:
            continu = fichier.read()
            if continu:
                print("Historique des calculs IMC :")
                print(continu)
            # si le fichier est vide
            else:
                print("Aucun historique disponible")
    # si le fichier nas pas ete cree
    except FileNotFoundError:
        print("Aucun historique disponible")
