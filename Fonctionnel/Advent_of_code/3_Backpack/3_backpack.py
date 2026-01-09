def lire_fichier(nom_fichier) : 
    with open(nom_fichier, "r", encoding="utf-8") as f : 
        return f.read()
    
# Quelle est la somme de l’objet prioritaire de chaque sac ?
def somme_sac(data) : 
    total = 0 
    #supprime les espaces au début et fin et sépare chaque elfe par une ligne
    lignes = data.strip().split("\n")
    for ligne in lignes : 
        centre = len(ligne) // 2 
        p1 = ligne[: centre] # : centre prend du caractere 0 au centre 
        p2 = ligne[centre :] # inversement
        same = set(p1) & set(p2) # set() pour chaque lettre est séparé et devient unique, et & pour avoir les caractères  
        # qui apparraissent dans les 2 poches 
        for string in same : 
            if 'a' <= string <= 'z' :
                total += ord(string) - ord('a') + 1 # donne la valeur en asci d'une lettre (a vaut 97 et z vaut 122 ex : 122 - 97 = 25) 
            else :
                total += ord(string) - ord('A') + 27
    return total

assert somme_sac(lire_fichier("backpack.txt")) == 8185

# Quelle est la somme des priorités des badges de chaque équipe ?
def badge(data) : 
    total = 0 
    lignes = data.strip().split("\n")
    for i in range(0, len(lignes), 3) : 
        # récupère les 3 équipes 
        e1 = lignes[i] # i correspond à la première ligne de chaque équipe
        e2 = lignes[i + 1]
        e3 = lignes[i + 2]
        same = set(e1) & set(e2) & set(e3)
        for string in same :
            if 'a' <= string <= 'z' :
                total += ord(string) - ord('a') + 1 # donne la valeur en asci d'une lettre (a vaut 97 et z vaut 122 ex : 122 - 97 = 25) 
            else :
                total += ord(string) - ord('A') + 27
    return total

assert badge(lire_fichier("backpack.txt")) == 2817

print(somme_sac(lire_fichier("backpack.txt")))
print(badge(lire_fichier("backpack.txt")))
        
            
                
