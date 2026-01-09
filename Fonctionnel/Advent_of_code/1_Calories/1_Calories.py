# Combien de calories porte l’elfe ayant le plus de calories dans son sac ?
def lire_fichier(nom_fichier) : 
    with open(nom_fichier, "r", encoding="utf-8") as f : 
        return f.read()
def max_calories(data) : 
    #supprime les espaces au début et fin et sépare chaque elfe par une ligne
    elfes = data.strip().split("\n\n") # .split() pour transformer une chaine de caractere en liste et .strip() pour supprimer 
    somme = []                         # les espaces au début et fin
    for val in elfes : 
        #decoupe chauqe elfe en lignes 
        ligne = val.split("\n") 
        # i.strip ignore les lignes vides 
        tot = sum(int(i) for i in ligne if i.strip() != "")
        somme.append(tot)
    return max(somme)

#Combien de calories totales portent les 3 elfes ayant le plus de calories dans leur sac ?

def somme_3_elfes(data) : 
    #supprime les espaces au début et fin et sépare chaque elfe par une ligne
    elfes = data.strip().split("\n\n")
    somme = []
    for val in elfes : 
        #decoupe chauqe elfe en lignes 
        ligne = val.split("\n")
        tot = sum(int(i) for i in ligne if i.strip() != "")
        somme.append(tot)
    #tri de liste
    somme.sort(reverse=True)
    return sum(somme[:3])

assert max_calories(lire_fichier("Calories_elfes.txt")) == 70509
assert somme_3_elfes(lire_fichier("Calories_elfes.txt")) == 208567

print("Le nombre de calorie que porte l'elfe avec le plus de calorie dans son sac est : ", max_calories(lire_fichier("Calories_elfes.txt")))
print("La somme de Calorie des 3 premiers elfes est de : ", somme_3_elfes(lire_fichier("Calories_elfes.txt")))

