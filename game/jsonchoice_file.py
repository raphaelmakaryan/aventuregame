import json


def historical(choice, textChapter, nameChapter):
    # Charger choice depuis le fichier JSON
    with open("save/choice.json", "r") as choice_file:
        choice_json = json.load(choice_file)

    # Créer une structure de choice
    structure = {
        "Chapter_name": nameChapter,
        "Text": textChapter["texte"],
        "Choice": choice,
    }

    # Ajouter la structure à l'historique
    choice_json["history"].append(structure)

    # Sauvegarder la mise à jour dans le fichier JSON
    with open("save/choice.json", "w") as choice_file:
        json.dump(choice_json, choice_file)
