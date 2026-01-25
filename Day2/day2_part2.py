# Première partie : identique à la résolution de la première moitié du défi
input_id = open("Day2/day2.txt").read().split(",")
res = 0

for elt in input_id:
    plage_min, plage_max = elt.split("-")
    for i in range(int(plage_min), int(plage_max) + 1):
        x = str(i)

        # Deuxième partie : Parcours du nombre à la recherche de motif
        for n in range(1, len(x)//2 + 1):
            if len(x) % n == 0:
                motif = x[:n]
                if motif * (len(x)//n) == x:
                    res += i
                    break

print(res)