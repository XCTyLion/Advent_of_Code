# Import du fichier
input_number = open("day1.txt").read().split("\n")

# Curseur au début
dial = 50

# Variable du resultat
res = 0

# Pour chaque ligne du fichier
for i in range(len(input_number)):
    # Le signe varie en fonction du premier caractère (L ou R)
    if input_number[i][0] == 'L':
        signe = -1
    else:
        signe = 1
    # On ajoute le nombre multiplié avec le décalage à gauche ou droite
    dial += (signe * int(input_number[i][1:]))

    # On ramène dial dans l'intervalle [0, 99]
    dial %= 100

    # Si dial vaut 0 on incrémente res
    if dial == 0:
        res += 1

# On affiche le résultat
print(res)