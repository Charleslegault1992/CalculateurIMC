#Créer un calculateur d'IMC avec différentes fonctionnalités
# Défis Avancés
# Gérer les merge conflicts sur main.py
# Utiliser Git Flow (branches feature/develop/main)
# Faire des rebases pour garder l'historique propre

def sauvegarder_calcul(nom, imc):
    # Sauvegarde dans un fichier
    with open("imc_historique.txt", "r", encoding="utf-8") as fichier:
        fichier.write(f"{nom}: {imc}\n")

def afficher_historique():
    # Lit le fichier
    while True:
        with open("imc_historique.txt", "r", encoding="utf-8") as fichier:
            continu = fichier.read()
            print("Historique des calculs IMC :")
            print(continu)
