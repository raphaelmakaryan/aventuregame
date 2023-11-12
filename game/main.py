# region IMPORT
import json
import xml.etree.ElementTree as ET
import game_file
import view_file

# endregion IMPORT

# region Load files
# //! Fonction pour charger le nom du chapitre actuel depuis le fichier de sauvegarde
def load_current_chapter_name():
    try:
        tree = ET.parse('game/character_characteristics.xml')
        root = tree.getroot()
        chapitre_actuel_element = root.find('chapitre_actuel')
        return chapitre_actuel_element.text
    except (FileNotFoundError, ET.ParseError):
        return "chapitre1"


# //! Charger l'histoire depuis le fichier JSON
def load_story_main():
    with open("history/history_file.json", "r", encoding='utf-8') as story_file:
        history = json.load(story_file)
        return history


# //! Charger les caractéristiques du personnage depuis le fichier XML
def load_character_characteristics():
    character_tree = ET.parse(
        "game/character_characteristics.xml", parser=ET.XMLParser(encoding="UTF-8")
    )
    character_root = character_tree.getroot()
    return character_root
# endregion Load files

# region Lancement du jeu
history = load_story_main()
character_root = load_character_characteristics()
main_menu_choice = view_file.main_menu()
if main_menu_choice != 0:
    game_file.main_game(load_current_chapter_name, history)
else:
    print("Le jeu s'arrête !")
# endregion Lancement du jeu