import json
import xml.etree.ElementTree as ET
def save_progress(current_chapter):
    try:
        tree = ET.parse('game/character_characteristics.xml')
        root = tree.getroot()
        chapitre_actuel_element = root.find('chapitre_actuel')
        chapitre_actuel_element.text = current_chapter
        tree.write('game/character_characteristics.xml')
    except (FileNotFoundError, ET.ParseError):
        print("Erreur lors de l'enregistrement de la progression.")