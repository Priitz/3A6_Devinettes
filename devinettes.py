#!/usr/bin/env python3
import random

MAX_ESSAIS = 10
MAX_RANGE = 100
CODE_VICTOIRE = 'GGG'
CODE_DEFAITE = 'PPP'

"""
Jeu de devinettes.

Par Jeremy Lalonde
"""


def main():

    print("""Bonjour, je m'apelle Jeremy 2020
J'ai choisi un nombre entier entre 1 et 100
Pouvez-vous le deviner?""")
    jeu()

def jeu():
    nbEssais = 1
    nombre = random.randint(1, MAX_RANGE)
    sequence = []
    while True:

        if nbEssais > MAX_ESSAIS:
            print("Désolé, vous avez échoué après 10 tentatives")
            print(f"Le nombre choisi était : {nombre}")
            break
        else:
            essai = (input(f"Essai {nbEssais}: "))
            if essai == CODE_DEFAITE:
                print(f"Désolé, vous avez échoué après {nbEssais} tentatives")
                print(f"Le nombre choisi était : {nombre}")
                rejouer()

            elif essai == CODE_VICTOIRE:
                print("Bravo, vous avez trouvé le nombre")
                sequence.append(essai)
                print(f"Votre séquence gagnante est: {sequence}")
                rejouer()

            else:
                if essai.lstrip('-+').isdigit():
                    nbEssais = nbEssais + 1
                    essai = int(essai)
                    if essai > nombre:
                        print("Votre nombre est trop grand...")
                        sequence.append(essai)
                    elif essai < nombre:
                        print("Votre nombre est trop petit...")
                        sequence.append(essai)
                    else:
                        print("Bravo, vous avez trouvé le nombre")
                        sequence.append(essai)
                        print(f"Votre séquence gagnante est: {sequence}")
                        rejouer()

                else:
                    print("Erreur : Entrez un nombre entier svp")

def rejouer():
    reponse = input("Voulez-vous rejouer? [O/N] ")
    if reponse.upper() == 'OUI' or reponse.upper() == 'O':
        jeu()
    elif reponse.upper() == 'NON' or reponse.upper() == 'N':
        print("Au revoir!")
        exit()
    else:
        print("Choix invalide")
        rejouer()

if __name__ == '__main__':
    main()
