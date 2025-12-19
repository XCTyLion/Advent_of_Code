# Défi Jour 1

## Première partie

Pour passer une porte vous avez besoin d'un mot de passe contenu dans un coffre fort. Ce dernier est composé d'un cadran allant de **0 à 99** dans l'ordre. A partir de la **séquence de rotation** qui vous est fournit vous devez parvenir à déterminer combien de fois le curseur tombe pile sur ``0``.

La séquence de rotation est constituée, pour chacune des lignes qui la compose, de la lettre ``'L'`` ou ``'R'`` donnant le sens de rotation (gauche pour L, droite pour R) suivi d'un chiffre indiquant le nombre de décalage à effectuer.

Par exemple, si le curseur est initialement sur ``11`` et que la première instruction est ``'R8'`` alors le cadran pointe désormais sur ``19``. Si la deuxième instruction est ``'L19'`` le cadran pointera sur ``0`` et le compteur sera incrémenté de ``1``.

Le cadran commence **toujours** par pointer sur **50**.

Voici une entrée de test (Les données sont dans le fichier day1_test.txt):

``L68``
``L30``
``R48``
``L5``
``R60``
``L55``
``L1``
``L99``
``R14``
``L82``

Ces rotations provoquerait le déplacement du cadran comme suit:
- Le cadran commence par pointer vers ``50``.
- Le cadran est tourné ``L68`` à pointer sur ``82``.
- Le cadran est tourné ``L30`` à pointer sur ``52``.
- Le cadran est tourné ``R48`` à pointer sur ``0``.
- Le cadran est tourné ``L5`` à pointer sur ``95``.
- Le cadran est tourné ``R60`` à pointer sur ``55``.
- Le cadran est tourné ``L55`` à pointer sur ``0``.
- Le cadran est tourné ``L1`` à pointer sur ``99``.
- Le cadran est tourné ``L99`` à pointer sur ``0``.
- Le cadran est tourné ``R14`` à pointer sur ``14``.
- Le cadran est tourné ``L82`` à pointer sur ``32``.

Le cadran pointe un total de 3 fois sur 0 au cours du processus, le **mot de passe** de cet exemple est donc **3**.

__________________________________________________________________________________________________________

## Deuxième partie

Malgré que vous ayez trouvé le bon mot de passe la porte ne s'ouvre pas. Vous comprenez alors qu'il faut compter le nombre de fois où le cadran **passe** par 0 au cours de **toutes les rotations** !

En reprenant l'exemple cela donnerai :

- Le cadran commence par pointer vers 50.
- Le cadran est tourné ``L68`` à pointer sur ``82``; au cours de cette rotation, il pointe à ``0`` une fois.
- Le cadran est tourné ``L30`` à pointer sur ``52``.
- Le cadran est tourné ``R48`` à pointer sur ``0``.
- Le cadran est tourné ``L5`` à pointer sur ``95``.
- Le cadran est tourné ``R60`` à pointer sur ``55``; au cours de cette rotation, il pointe à ``0`` une fois.
- Le cadran est tourné ``L55`` à pointer sur ``0``.
- Le cadran est tourné ``L1`` à pointer sur ``99``.
- Le cadran est tourné ``L99`` à pointer sur ``0``.
- Le cadran est tourné ``R14`` à pointer sur ``14``.
- Le cadran est tourné ``L82`` à pointer sur ``32``; au cours de cette rotation, il pointe à ``0`` une fois.

Au total, le cadran passe 6 fois sur **0**. Le **mot de passe** est donc **6**.






