#!/usr/bin/env python3
import random
"""
Jeu de devinettes.

Par Jeremy Lalonde
"""


def main():
    nbEssais = 1
    nombre = random.randint(1, 100)
    print("""Bonjour, je m'apelle Jeremy 2020
J'ai choisi un nombre entier entre 1 et 100
Pouvez-vous le deviner?""")
    essai = int(input(f"Essai {nbEssais}: "))
    while essai != nombre:
        if essai > nombre:
            print("Votre nombre est trop grand...")
            essai = int(input(f"Essai {nbEssais}: "))
            nbEssais = nbEssais + 1
        elif essai < nombre:
            print("Votre nombre est trop petit...")
            essai = int(input(f"Essai {nbEssais}: "))
            nbEssais = nbEssais + 1
        elif essai == nombre:
            print("Bravo, vous avez deviné le nombre")

    print("Bravo, vous avez trouvé le nombre")










if __name__ =='__main__':
        main()
