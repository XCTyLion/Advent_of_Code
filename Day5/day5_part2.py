
# Lecture du fichier d'entrée
input_number = open("Day5/day5_test.txt").read().split("\n")

# Intervalles de valeurs
plages = []

# Ajoute les intervalles sous forme de tuple d'entier
for elt in input_number:
    if "-" in elt:
        start, end = map(int, elt.split("-"))
        plages.append((start, end))


# Tri les intervalles par ordre croissant de l'identifiant de début
plages.sort(key=lambda x: x[0])

# Intervalle fusionné
fusion = []

# Parcours des intervalles
for start, end in plages:

    # Si la liste est vide ou que l'id du début de l'intervalle est supérieur à l'id de fin de l'intervalle fusionné
    if not fusion or start > fusion[-1][1] + 1:
        fusion.append([start, end])
    
    # Sinon on fusionne les intervalles
    else:
        fusion[-1][1] = max(fusion[-1][1], end)

print(sum(end - start + 1 for start, end in fusion))