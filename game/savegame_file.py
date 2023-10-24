import json
def save_progress(current_chapter):
    progression = {"chapitre_actuel": current_chapter}
    with open("save/save_file.json", "w") as backup_file:
        json.dump(progression, backup_file)