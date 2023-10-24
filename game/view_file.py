import gameplay_file


# //!  Fonction pour afficher un chapitre et ses choix
def show_chapter(chapter):
    print(chapter["texte"])

    if "choix" in chapter and len(chapter["choix"]) > 0:
        print("Choix disponibles:")
        for i, choice in enumerate(chapter["choix"]):
            print(f"{i + 1}. {choice['texte']}")
    else:
        return

# //!  Fonction d'affichage du menu principal
def main_menu():
    print("Menu principal : \n1. Nouvelle Partie\n2. Continuer la Partie\nm. Quitter le jeu")
    user_choice = input()
    if user_choice == "m":
        #Sortir du jeu
        return 0
    elif user_choice == "1":
        gameplay_file.new_game()
        return 1
    elif user_choice == "2":
        return 2
    else:
        print("Vous n'avez pas effectué un bon choix")
        return main_menu()