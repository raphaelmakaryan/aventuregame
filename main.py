import os
import time
import random


def clear_console():
    # Vérifiez le système d'exploitation et exécutez la commande appropriée pour effacer la console
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour les systèmes Unix (Linux, macOS)
        os.system('clear')

texte = "Bonjour, comment ça va ?"

clear_console()  # Efface la console avant d'afficher le texte

for caractere in texte:
    print(caractere, end='', flush=True)
    time.sleep(0.1)

print()  # Pour ajouter un saut de ligne à la fin

choix = input("""
1. choix 1
2. choix 2 (dé)
""")

def lanceDe():
    return random.randint(1, 6)


if choix == 1:
    print(choix)
else:
    print("Le dé est = " + str(lanceDe()))
