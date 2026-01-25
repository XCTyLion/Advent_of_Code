"""Script pour identifier et sommer les IDs invalides.

Un ID est considéré invalide s'il est composé d'une séquence de chiffres
répétée deux fois (ex. 55, 6464, 123123).
Les IDs sont fournis sous forme de plages (min-max) séparées par des virgules.
"""

# Import des données à traiter
input_id = open("day2.txt").read().split(",")

# Variable pour accumuler la somme des IDs invalides
res = 0

# Parcours de chaque plage d'IDs
for elt in input_id:
    # Séparation de la borne minimale et maximale de la plage
    plage_min, plage_max = elt.split("-")

    # Boucle sur tous les IDs de la plage (inclusif)
    for i in range(int(plage_min), int(plage_max) + 1):
        x = str(i)  # Conversion de l'ID en chaîne de caractères

        # Vérifie si la première moitié de l'ID est égale à la seconde moitié
        if x[0 : len(plage_max) // 2] == x[len(plage_max) // 2:]:
            res += i  # Ajoute l'ID invalide à la somme

# Affiche la somme totale des IDs invalides
print(res)
