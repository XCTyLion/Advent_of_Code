# Lecture du fichier d'entrée
input_number = open("Day3/day3.txt").read().split("\n")

# Variable de résultat final
res = 0

# Itération sur toutes les séquences de chiffre du fichier
for banque in input_number:
    #Pile des chiffres retenu pour la sous séquence max
    pile = []
    
    # Longueur de la sous séquence souhaité
    to_take = 12

    # Parcours de chaque chiffre
    for i in range(len(banque)):

        # Vérifie si la chiffre actuel peut faire partie de la sous séquence maximal
        while pile and pile[-1] < banque[i] and (len(pile) - 1 + len(banque) - i) >= to_take:
            pile.pop()
        
        # Si la pile le permet on ajoute le chiffre à la pile
        if len(pile) < to_take:
            pile.append(banque[i])
        
        # Sinon l'élément n'est pas intéressant
        else:
            pass
    
    # Calcul de la sous séquence maximale
    res += int(''.join(pile))

print("Joltage total:", res)