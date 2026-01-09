# Somme récursive
# Écrire une fonction récursive somme(n) qui retourne la somme des entiers de 1 à n.
# Contraintes :
# - Utiliser uniquement la récursion
# - Prévoir un cas de base
# - n est un entier positif ou nul

def somme(n) :
    if n == 1 :
        return 1
    elif n == 0 : 
        return 0
    else :
        return n + somme(n - 1)

assert somme(3) == 6

# Liste 
# Écrire une fonction récursive somme_liste(L) qui calcule la somme des éléments d’une liste d’entiers.
# Contraintes :
# - Ne pas utiliser de boucle
# - Traiter une liste vide correctement

def somme_liste(l) : 
    if l == [] :
        return 0
    else : 
        return l[0] + somme_liste(l.remove(l[0]))

print(somme_liste([3, 2, 1]))
