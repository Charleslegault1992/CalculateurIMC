#Créer un calculateur d'IMC avec différentes fonctionnalités
# Défis Avancés
# Gérer les merge conflicts sur main.py
# Utiliser Git Flow (branches feature/develop/main)
# Faire des rebases pour garder l'historique propre

def calculer_imc(poids, taille):
    # IMC = poids / taille²
    return poids / ((taille/100)**2)


def interpreter_imc(imc):
    # Retourne la catégorie : maigre , normail , surpoids , obeisite
    if imc < 18.5:
        return "Maigre"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obesite"

