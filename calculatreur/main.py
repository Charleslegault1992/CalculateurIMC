#Créer un calculateur d'IMC avec différentes fonctionnalités
# Défis Avancés
# Gérer les merge conflicts sur main.py
# Utiliser Git Flow (branches feature/develop/main)
# Faire des rebases pour garder l'historique propre

import interface
import historique
import calculs

print("1 = Nouveau calculs            2 = Historique des IMC")
choix = int(input("Entrer un choix :"))

if choix == 1 :
    nom = input("Entrer votre nom : ")
    poid , taille = interface.demander_infos()
    imc = calculs.calculer_imc(poid, taille)
    categorie = calculs.interpreter_imc(imc)
    historique.sauvegarder_calcul(nom, imc)
    print(interface.afficher_resultat(imc, categorie))

elif choix == 2:
    historique.afficher_historique()

else:
    print("Choix invalide !")

