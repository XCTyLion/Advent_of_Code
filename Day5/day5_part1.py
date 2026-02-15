# Lecture du fichier d'entrée
input_number = open("Day5/day5_test.txt").read().split("\n")

# Intervalles de valeurs
plages = []

# Identifiants à tester
identifiant = []

swap = False

# Lis le fichier d'entrée et met les intervalles dans plages et les identifiants à tester dans identifiant 
for elt in input_number:

    # Savoir si la veleur lu est un intervalle ou un identifiant
    if elt == "":
        swap = True

    # Ajoute l'intervalle
    elif not swap:
        plages.append(elt)

    # Ajoute l'identifiant
    else:
        identifiant.append(elt)

def est_valide(elt):
    """
    Test la validité d'un identifiant

    @param elt identifiant à tester
    @return 1 si identifiant valide, 0 sinon
    """
    for plage in plages:
        val_min, val_max = plage.split("-")
        if int(val_min) <= int(elt) <= int(val_max):
            return 1
    return 0

# Variable de résultat final
res = 0

# Compte le nombre d'identifiant valide
for elt in identifiant:
    res += est_valide(elt)    
        
print(res)
