# Lecture du fichier d'entrée
input_maze = open("day4.txt").read().split("\n")

# Liste des directions possibles
autre = [(1,0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1)]

# Total
res = 0

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
                res += 1
    
print(res)