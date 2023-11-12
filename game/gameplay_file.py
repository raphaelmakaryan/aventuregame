import savegame_file
import random
import os
import json
import xml.etree.ElementTree as ET

def modifier_nom_personnage(nouveau_nom):
    # Charger le fichier XML
    tree = ET.parse('game/character_characteristics.xml')
    root = tree.getroot()

    # Trouver l'élément 'nom' et le modifier avec le nouveau nom
    nom_element = root.find('nom')
    nom_element.text = nouveau_nom

    # Enregistrer les modifications dans le fichier XML
    tree.write('game/character_characteristics.xml')

# //! Jeu du dée
def dice_game(dice_game, character_characteristic):
    minimum_value = dice_game["valeur_minimale"]
    result_lancer_dice = random.randint(
        1, 6
    )  # Lancer de dé 6 faces (vous pouvez ajuster la portée)

    # Ajoutez des modifications en fonction de la caractéristique du personnage (par exemple, force)
    # Pour cet exemple, nous supposons une modification fixe de +2 pour la caractéristique "force".
    characteristic_modification = 2  # Modifiez selon vos besoins.

    total_lancer_dice = result_lancer_dice + characteristic_modification

    if total_lancer_dice >= minimum_value:
        print("Vous avez réussi le lancer de dé !")
        return True
    else:
        print("Vous avez échoué le lancer de dé...")
        return False


# //!   Fonction pour démarrer une nouvelle partie
def new_game():
    initial_data = {"history": []}
    nouveau_nom = input("Entrez le nouveau nom de votre personnage : ")
    modifier_nom_personnage(nouveau_nom)
    if not os.path.exists("save/choice.json"):
        with open("save/choice.json", "w") as json_file:
            json.dump(initial_data, json_file)
    else:
        with open("save/choice.json", "w") as json_file:
            json.dump(initial_data, json_file)
        savegame_file.save_progress("chapitre1")


# //!   Fonction pour continuer une partie
def continue_game(current_chapter_name, history):
    try:
        return history["chapitres"][current_chapter_name]
    except:
        print("Erreur de la fonction de continuation de la partie !")
