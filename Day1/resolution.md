# Résolution 

---

## Partie 1 : Compter les passages exacts sur 0

### Principe
On parcourt chaque instruction et on vérifie si, **après chaque rotation complète**, le cadran pointe exactement sur 0.

### Algorithme (fonction `partie1`)
1. **Initialisation**
   - Position initiale : `dial = 50`
   - Compteur : `res = 0`

2. **Pour chaque instruction**
   - Extraire le sens (`R` ou `L`) et le nombre de crans (`move`).
   - Mettre à jour la position :
     - Si `R` : `dial = (dial + move) % 100`
     - Si `L` : `dial = (dial - move) % 100`
   - Si `dial == 0` : incrémenter `res`.

3. **Résultat**
   - `res` contient le nombre de fois où le cadran a pointé exactement sur 0 après une rotation.

---

## Partie 2 : Compter tous les passages par 0

---

### Solution 1 : Brute-force (fonction `partie2_brute_force`)

#### Principe
Pour chaque instruction, on simule **chaque cran de rotation** un par un, et on compte chaque passage par 0.

#### Algorithme
1. **Initialisation**
   - Position initiale : `dial = 50`
   - Compteur : `res = 0`

2. **Pour chaque instruction**
   - Extraire le sens et `move`.
   - Pour chaque cran de `1` à `move` :
     - Si `R` : `dial = (dial + 1) % 100`
     - Si `L` : `dial = (dial - 1) % 100`
     - Si `dial == 0` : incrémenter `res`.

3. **Résultat**
   - `res` contient le nombre total de passages par 0, y compris pendant les rotations.

#### Exemple
Pour `R60` avec `dial = 95` :
- On incrémente `dial` de 1, 60 fois, et on compte chaque passage par 0.

---

### Solution 2 : Optimisée (fonction `partie2_optimisee`)

#### Principe
On calcule mathématiquement le nombre de passages par 0 pendant une rotation, sans simuler chaque cran.

#### Algorithme
1. **Initialisation**
   - Position initiale : `dial = 50`
   - Compteur : `res = 0`

2. **Pour chaque instruction**
   - Extraire le sens et `move`.
   - Calculer la distance jusqu’au prochain 0 (`first`) :
     - Si `R` : `first = (100 - dial) % 100` (si `first == 0`, alors `first = 100`)
     - Si `L` : `first = dial % 100` (si `first == 0`, alors `first = 100`)
   - Si `move >= first` :
     - `res += 1 + (move - first) // 100`
   - Mettre à jour `dial` :
     - Si `R` : `dial = (dial + move) % 100`
     - Si `L` : `dial = (dial - move) % 100`

3. **Résultat**
   - `res` contient le nombre total de passages par 0, calculé de manière optimale.

#### Exemple
Pour `R60` avec `dial = 95` et `res = 0`:
- `first = (100 - 95) % 100` → `first = 5`
- `move >= first` 
    - `res += 1 + (60 - 5) // 100`
    - `res = 1`
- Nouvelle position : `dial = (95 + 60) % 100 ` → `dial = 55`