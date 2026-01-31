# Lecture du fichier d'entrée
input_maze = open("Day4/day4.txt").read().split("\n")

# Lecture du fichier d'entrée
prochain = open("Day4/day4.txt").read().split("\n")

# Liste des directions possibles
autre = [(1,0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1)]

# Inisialisation du résultat
res = 0

ajout = True

# Tant qu'il y a eu des modifications à l'itération d'avant on continue
while ajout:

    # Inisialisation du résultat de l'état actuel
    res_tab = 0

    # Parcours des caractères d'entrés
    for i in range(len(input_maze)):
        for j in range(len(input_maze[i])):

            # Vérifie la présence d'un cadeau à l'indice [i][j]
            if input_maze[i][j] == '@':        

                # Initialisation du compteur 
                total_char = 0
                
                # Parcours des directions
                for elt in autre:

                    # Compte le nombre de cadeau présent à une distance de un autour de l'élément [i][j]
                    if 0 <= i + elt[1] < len(input_maze) and 0 <= j + elt[0] < len(input_maze[i]):
                        if input_maze[i + elt[1]][j + elt[0]] == '@':
                            total_char += 1

                # Si l'espace est suffisant le résultat est incrémenté
                if total_char < 4:
                    res_tab += 1

                    # Mise à jour du prochain état à traiter
                    prochain[i] = prochain[i][:j] + '.' + prochain[i][j+1:]

    # Si rien n'a été modifié on arrête
    if res_tab == 0:
        ajout = False

    # Le prochain état devient l'actue
    input_maze = prochain

    # Incrémentation du résultat
    res += res_tab
    
print(res)