import json
import xml.etree.ElementTree as ET
import random

# Fonction pour charger le nom du chapitre actuel depuis le fichier de sauvegarde
def charger_nom_chapitre_actuel():
    try:
        with open('sauvegarde.json', 'r') as fichier_sauvegarde:
            progression = json.load(fichier_sauvegarde)
        return progression.get('chapitre_actuel', 'chapitre1')
    except (FileNotFoundError, json.JSONDecodeError):
        return 'chapitre1'

# Fonction pour enregistrer la progression du joueur dans le fichier de sauvegarde
def enregistrer_progression(chapitre_actuel):
    progression = {'chapitre_actuel': chapitre_actuel}
    with open('sauvegarde.json', 'w') as fichier_sauvegarde:
        json.dump(progression, fichier_sauvegarde)

# Charger l'histoire depuis le fichier JSON
with open('histoire.json', 'r') as fichier_histoire:
    histoire = json.load(fichier_histoire)

# Charger les caractéristiques du personnage depuis le fichier XML
arbre_personnage = ET.parse('caracteristiques_personnage.xml')
racine_personnage = arbre_personnage.getroot()


def choix_jeu_de_de(jeu_de_de, caracteristique_personnage):
    valeur_minimale = jeu_de_de['valeur_minimale']
    resultat_lancer_de = random.randint(1, 20)  # Lancer de dé 20 faces (vous pouvez ajuster la portée)

    # Ajoutez des modifications en fonction de la caractéristique du personnage (par exemple, force)
    # Pour cet exemple, nous supposons une modification fixe de +2 pour la caractéristique "force".
    modification_caracteristique = 2  # Modifiez selon vos besoins.

    total_lancer_de = resultat_lancer_de + modification_caracteristique

    if total_lancer_de >= valeur_minimale:
        print("Vous avez réussi le lancer de dé !")
        return True
    else:
        print("Vous avez échoué le lancer de dé...")
        return False


# Initialisez la variable nom_chapitre_actuel au début du programme
nom_chapitre_actuel = charger_nom_chapitre_actuel()

# Fonction pour afficher un chapitre et ses choix
def afficher_chapitre(chapitre):
    print(chapitre['texte'])
    print("Choix disponibles:")
    for i, choix in enumerate(chapitre['choix']):
        print(f"{i + 1}. {choix['texte']}")

# Boucle principale du jeu
while True:
    chapitre_actuel = histoire['chapitres'][nom_chapitre_actuel]

    afficher_chapitre(chapitre_actuel)
    choix_utilisateur = input("Faites un choix (1, 2, ... ou q pour quitter) : ")

    if choix_utilisateur == 'q':
        break

    choix_index = int(choix_utilisateur) - 1
    if 0 <= choix_index < len(chapitre_actuel['choix']):
        choix = chapitre_actuel['choix'][choix_index]

        if 'jeu_de_de' in choix:
            jeu_de_de = choix['jeu_de_de']
            caracteristique_personnage = 10  # Remplacez cette valeur par la caractéristique réelle du personnage
            if choix_jeu_de_de(jeu_de_de, caracteristique_personnage):
                nom_chapitre_actuel = choix['destination']
                enregistrer_progression(nom_chapitre_actuel)
        else:
            nom_chapitre_actuel = choix['destination']
            enregistrer_progression(nom_chapitre_actuel)
    else:
        print("Choix invalide. Veuillez choisir un numéro valide ou 'q' pour quitter.")