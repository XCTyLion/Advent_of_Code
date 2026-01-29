# Lecture du fichier d'entrée
input_number = open("Day3/day3.txt").read().split("\n")

# Variable de résultat final
res = 0

# Itération sur toutes les séquences de chiffre du fichier
for banque in input_number:
    
    # Initialisation du max de la séquence
    maxi = 0

    # Itération sur la séquence de chiffre
    for i in range(len(banque) - 1):
        for j in range(i+ 1, len(banque)):
            
            # maximum prend la valeur du plus grand nombre 
            if int(banque[i] + banque[j]) > maxi:
                maxi = int(banque[i] + banque[j])
    
    # Ajout du maximum de la ligne au résulta
    res += maxi

print("Résultat :",res)