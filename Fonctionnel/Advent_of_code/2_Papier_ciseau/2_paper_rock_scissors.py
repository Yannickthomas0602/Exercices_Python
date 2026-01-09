def lire_fichier(nom_fichier) : 
    with open(nom_fichier, "r", encoding="utf-8") as f : 
        return f.read()

# Quel sera votre score total à la fin du championnat ? (système classique)
def score_classique(data : str) -> int :
    # dictionnaire qui contient le système de points
    points = {
        'A X': 4, 'A Y': 8, 'A Z': 3,
        'B X': 1, 'B Y': 5, 'B Z': 9,
        'C X': 7, 'C Y': 2, 'C Z': 6
    } 
    total = 0
    #supprime les espaces au début et fin et sépare chaque elfe par une ligne
    lignes = data.strip().split("\n")
    # parcours chaque ligne pour calculer le score total
    for ligne in lignes :
        total += points.get(ligne) #.get() pour obtenir la valeur associée à la clé
    return total
assert score_classique(lire_fichier("papier_ciseau.txt")) == 13005

# Quel sera votre score total à la fin du championnat ? (Mauvaise lecture)
def score_mauv_lect(data : str) -> int : 
    # Même principe mais le dictionnaire de points est différent 
    points = {
        'A X': 3, 'A Y': 4, 'A Z': 8,
        'B X': 1, 'B Y': 5, 'B Z': 9,
        'C X': 2, 'C Y': 6, 'C Z': 7
    } 
    total = 0
    #supprime les espaces au début et fin et sépare chaque elfe par une ligne
    lignes = data.strip().split("\n")
    # parcours chaque ligne pour calculer le score total
    for ligne in lignes : 
        total += points.get(ligne) #.get() pour obtenir la valeur associée à la clé
    return total

assert score_mauv_lect(lire_fichier("papier_ciseau.txt")) == 11373

print(score_classique(lire_fichier("papier_ciseau.txt")))
print(score_mauv_lect(lire_fichier("papier_ciseau.txt")))
