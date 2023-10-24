import savegame_file
import random
import os
import json


# //! Jeu du dée
def dice_game(dice_game, character_characteristic):
    minimum_value = dice_game["valeur_minimale"]
    result_lancer_dice = random.randint(
        1, 20
    )  # Lancer de dé 20 faces (vous pouvez ajuster la portée)

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
