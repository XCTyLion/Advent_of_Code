# On lit le contenu des fichiers et on découpe chaque ligne en une liste
# Chaque ligne correspond à une instruction de déplacement (ex: "R10" ou "L25")
input_number = open("Day1/day1.txt").read().split("\n")
input_number_test = open("Day1/day1_test.txt").read().split("\n")

# Position initiale du curseur sur le cadran (de 0 à 99)
dial = 50

# Résultat initial (nombre de fois où l’on passe par 0)
res = 0


def resolution(input, dial):
    """
    Version optimisée : calcule directement combien de fois on passe par 0
    sans simuler chaque pas.
    """
    res = 0
    # On parcourt chaque instruction de la liste
    for i in range(len(input)):
        # Nombre de pas à effectuer (on enlève la première lettre 'R' ou 'L')
        move = int(input[i][1:])

        # Détermination de la direction
        if input[i][0] == 'R':  # Déplacement vers la droite
            signe = 1
            # Distance jusqu’au prochain passage par 0
            first = (100 - dial) % 100
            if first == 0:
                first = 100
        else:  # Déplacement vers la gauche
            signe = -1
            # Distance jusqu’au prochain passage par 0
            first = dial % 100
            if first == 0:
                first = 100

        # Si le mouvement est assez grand pour atteindre 0
        if move >= first:
            # On compte le premier passage + les tours complets supplémentaires
            res += 1 + (move - first) // 100

        # Mise à jour de la position du curseur (modulo 100 pour rester sur le cadran)
        dial += signe * move % 100

    return res


def resolution2(input, dial):
    """
    Version brute-force : simule chaque pas un par un.
    """
    res = 0
    # On parcourt chaque instruction de la liste
    for i in range(len(input)):
        # Détermination de la direction
        if input[i][0] == 'L':
            signe = -1
        else:
            signe = 1

        # On simule chaque pas du déplacement
        for j in range(int(input[i][1:])):
            dial += signe * 1      # On avance d’un pas
            dial %= 100            # On reste dans la plage [0, 99]
            if dial == 0:          # Si on passe par 0
                res += 1           # On incrémente le compteur
    return res


# Comparaison des deux méthodes sur les fichiers réels et de test
print(resolution(input_number, 50))       # Version optimisée
print(resolution(input_number_test, 50))  # Version optimisée avec fichier test
print(resolution2(input_number, 50))      # Version brute-force
print(resolution2(input_number_test, 50)) # Version brute-force avec fichier test

print((95 + 60) % 100)