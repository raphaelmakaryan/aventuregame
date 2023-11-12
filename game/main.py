# region IMPORT
import json
import xml.etree.ElementTree as ET
import random
# endregion IMPORT

def modifier_nom_personnage(nouveau_nom):
    # Charger le fichier XML
    tree = ET.parse('game/character_characteristics.xml')
    root = tree.getroot()

    # Trouver l'élément 'nom' et le modifier avec le nouveau nom
    nom_element = root.find('nom')
    nom_element.text = nouveau_nom

    # Enregistrer les modifications dans le fichier XML
    tree.write('game/character_characteristics.xml')

def md_creation():
    with open("save/choix.json") as history:
        history_json = json.load(history)

    markdown_content = ""

    for chapter in history_json["history"]:
        markdown_content += f"# {chapter['Chapter_name']} \n"
        markdown_content += f"### {chapter['Text']} \n"
        markdown_content += f"### {chapter['Choice']} \n\n"

    with open("save/history.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

# region Load files
# //! Fonction pour charger le nom du chapitre actuel depuis le fichier de sauvegarde
def charger_nom_chapitre_actuel():
    try:
        tree = ET.parse('game/character_characteristics.xml')
        root = tree.getroot()
        chapitre_actuel_element = root.find('chapitre_actuel')
        return chapitre_actuel_element.text
    except (FileNotFoundError, ET.ParseError):
        return "chapitre1"

# //! Charger l'histoire depuis le fichier JSON
def charger_histoire_principal():
    with open("history/history_file.json", "r") as fichier_histoire:
        histoire = json.load(fichier_histoire)
        return histoire

# //! Charger les caractéristiques du personnage depuis le fichier XML
def charger_caracteristiques_personnage():
    arbre_personnage = ET.parse(
        "game/character_characteristics.xml", parser=ET.XMLParser(encoding="UTF-8")
    )
    racine_personnage = arbre_personnage.getroot()
    return racine_personnage

# endregion Load files

# region Save Progression
# //! Fonction pour enregistrer la progression du joueur dans le fichier de sauvegarde
def enregistrer_progression(chapitre_actuel):
    try:
        tree = ET.parse('game/character_characteristics.xml')
        root = tree.getroot()
        chapitre_actuel_element = root.find('chapitre_actuel')
        chapitre_actuel_element.text = chapitre_actuel
        tree.write('game/character_characteristics.xml')
    except (FileNotFoundError, ET.ParseError):
        print("Erreur lors de l'enregistrement de la progression.")

def resetChoice():
    struct = {
        "history": []
    }

    with open("save/choix.json", "w") as history:
        json.dump(struct, history)

# endregion Save Progression

# region Gameplay
# //! Jeu du dée
def choix_jeu_de_de(jeu_de_de, caracteristique_personnage):
    valeur_minimale = jeu_de_de["valeur_minimale"]
    resultat_lancer_de = random.randint(
        1, 20
    )  # Lancer de dé 20 faces (vous pouvez ajuster la portée)

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
# //!   Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    nouveau_nom = input("Entrez le nouveau nom de votre personnage : ")
    modifier_nom_personnage(nouveau_nom)

    enregistrer_progression("chapitre1")

# //!   Fonction pour continuer une partie
def continuer_partie(nom_chapitre_actuel):
    return histoire["chapitres"][nom_chapitre_actuel]
# endregion Mini jeu

# region View
# //!  Fonction pour afficher un chapitre et ses choix
def afficher_chapitre(chapitre):
    print(chapitre["texte"])

    if "choix" in chapitre and len(chapitre["choix"]) > 0:
        print("Choix disponibles:")
        for i, choix in enumerate(chapitre["choix"]):
            print(f"{i + 1}. {choix['texte']}")
    else:
        return

# //!  Fonction d'affichage du menu principal
def menu_principal():
    print("Menu principal : \n1. Nouvelle Partie\n2. Continuer la Partie\nq. Quitter le jeu")
    choix_utilisateur = input()
    if choix_utilisateur == "q":
        #Sortir du jeu
        return 0
    elif choix_utilisateur == "1":
        resetChoice()
        nouvelle_partie()
        return 1
    elif choix_utilisateur == "2":
        return 2
    else:
        print("Vous n'avez pas effectué un bon choix")
        return menu_principal()
# endregion View

# region FICHIER JSON CHOIX
# try:
#     with open("save/choix.json", "r") as fichier_sauvegarde:
#         choix_utilisateur_save = json.load(fichier_sauvegarde)
# except FileNotFoundError:
#     choix_utilisateur_save = []
# endregion FICHIER JSON CHOIX


def test(choix, texteChapitre, nomChapitre):
    # Charger choix depuis le fichier JSON
    with open("save/choix.json", "r") as fichier_choix:
        choix_json = json.load(fichier_choix)

    # Créer une structure de choix
    structure = {
        "Chapter_name": nomChapitre,
        "Text": texteChapitre["texte"],
        "Choice": choix,
    }

    # Ajouter la structure à l'historique
    choix_json["history"].append(structure)

    # Sauvegarder la mise à jour dans le fichier JSON
    with open("save/choix.json", "w") as fichier_choix:
        json.dump(choix_json, fichier_choix)



# region Game
# //! Boucle principale du jeu
def main_game():
    # //! Initialisez la variable nom_chapitre_actuel au début du programme
    nom_chapitre_actuel = charger_nom_chapitre_actuel()
    while True:
        chapitre_actuel = continuer_partie(nom_chapitre_actuel)
        afficher_chapitre(chapitre_actuel)

        if nom_chapitre_actuel.startswith("fin"):
            test("", chapitre_actuel, nom_chapitre_actuel)
            md_creation()
            resetChoice()
            break

        choix_utilisateur = input("Faites un choix (1, 2 ou m pour retourner au menu principal) : ")

        if choix_utilisateur == "m":
            choix_menu_principal = menu_principal()
            if choix_menu_principal == 0:
                break
            main_game()
            break

        choix_index = int(choix_utilisateur) - 1
        if 0 <= choix_index < len(chapitre_actuel["choix"]):
            choix = chapitre_actuel["choix"][choix_index]

            # choix_utilisateur_save.append(choix_utilisateur)
            
            test(choix["texte"], chapitre_actuel, nom_chapitre_actuel)
            # test(choix_utilisateur_save, chapitre_actuel)

            if "jeu_de_de" in choix:
                jeu_de_de = choix["jeu_de_de"]
                caracteristique_personnage = 10  # Remplacez cette valeur par la caractéristique réelle du personnage
                if choix_jeu_de_de(jeu_de_de, caracteristique_personnage):
                    if choix_jeu_de_de(jeu_de_de, caracteristique_personnage):
                        nom_chapitre_actuel = jeu_de_de["True"]["destination"]
                        enregistrer_progression(nom_chapitre_actuel)
                    elif (
                        choix_jeu_de_de(jeu_de_de, caracteristique_personnage) == False
                    ):
                        nom_chapitre_actuel = jeu_de_de["False"]["destination"]
                        enregistrer_progression(nom_chapitre_actuel)
            else:
                nom_chapitre_actuel = choix["destination"]
                enregistrer_progression(nom_chapitre_actuel)
        else:
            print(
                "Choix invalide. Veuillez choisir un numéro valide ou 'q' pour quitter."
            )
# endregion Game

# region Lancement du jeu
histoire = charger_histoire_principal()
racine_personnage = charger_caracteristiques_personnage()
choix_menu_principal = menu_principal()
if choix_menu_principal != 0:
    main_game()
else:
    print("Le jeu s'arrête !")
# endregion Lancement du jeu
