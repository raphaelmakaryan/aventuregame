import gameplay_file
import view_file
import jsonchoice_file
import savegame_file
import json

def md_creation():
    with open("save/choice.json") as history:
        history_json = json.load(history)

    markdown_content = ""

    for chapter in history_json["history"]:
        markdown_content += f"# {chapter['Chapter_name']} \n"
        markdown_content += f"### {chapter['Text']} \n"
        markdown_content += f"### {chapter['Choice']} \n\n"

    with open("save/history.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

# //! Boucle principale du jeu
def main_game(load_current_chapter_name, history):
    # //! Initialisez la variable current_chapter_name au début du programme
    current_chapter_name = load_current_chapter_name()
    if current_chapter_name.startswith("fin") or current_chapter_name == "":
        gameplay_file.new_game()
        current_chapter_name = load_current_chapter_name()
    while True:
        current_chapter = gameplay_file.continue_game(current_chapter_name, history)
        view_file.show_chapter(current_chapter)


        if current_chapter_name.startswith("fin") or current_chapter_name == "":
            jsonchoice_file.historical("", current_chapter, current_chapter_name)
            md_creation()
            break

        user_choice = input(
            "Faites un choix (1, 2 ou m pour retourner au menu principal) : "
        )

        print()

        if user_choice == "m":
            main_menu_choice = view_file.main_menu()
            if main_menu_choice == 0:
                break
            main_game(load_current_chapter_name, history)
            break

        choice_index = int(user_choice) - 1
        if 0 <= choice_index < len(current_chapter["choix"]):
            choice = current_chapter["choix"][choice_index]

            jsonchoice_file.historical(choice["texte"], current_chapter, current_chapter_name)

            if "jeu_de_de" in choice:
                dice_game = choice["jeu_de_de"]
                character_characteristic = 10  # Remplacez cette valeur par la caractéristique réelle du personnage
                if gameplay_file.dice_game(dice_game, character_characteristic):
                    current_chapter_name = dice_game["True"]["destination"]
                    savegame_file.save_progress(current_chapter_name)
                else:
                    current_chapter_name = dice_game["False"]["destination"]
                    savegame_file.save_progress(current_chapter_name)
                print()
            else:
                current_chapter_name = choice["destination"]
                savegame_file.save_progress(current_chapter_name)
        else:
            print(
                "Choix invalide. Veuillez choisir un numéro valide ou 'm' pour quitter."
            )