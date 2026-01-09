def lire_fichier(nom_fichier) : 
    with open(nom_fichier, "r", encoding="utf-8") as f : 
        return f.read()
#Combien de paires d’elfes ont l’un de leur elfe avec sa section contenu dans la section de l’autre elfe ?
def sections(data) : 
    lignes = data.strip().split("\n")
    n = 0
    for val in lignes : 
        paire = val.split(",") #.split() pour séparer chaque paire d'elfe
        e1 = paire[0].split("-") #.split() pour séparer les sections des elfes 
        e2 = paire[1].split("-") #même chose
        debut_e1 = int(e1[0]) #début section elfe  
        fin_e1 = int(e1[1])   #fin section elfe 
        debut_e2 = int(e2[0])
        fin_e2 = int(e2[1])
        #vérifie si une section est dans l'autre paire
        if (debut_e1 >= debut_e2 and fin_e1 <= fin_e2) or (debut_e2 >= debut_e1 and fin_e2 <= fin_e1) : 
            n+=1
    return n

assert sections(lire_fichier("cleaning.txt")) == 448

# Combien de paires se superposent ?
def superpose(data) : 
    lignes = data.strip().split("\n")
    n = 0
    for val in lignes : 
        #même principe pour créer les variables 
        paire = val.split(",") #.split() pour séparer chaque paire d'elfe
        e1 = paire[0].split("-") #.split() pour séparer les sections des elfes 
        e2 = paire[1].split("-") #même chose
        debut_e1 = int(e1[0]) #début section elfe  
        fin_e1 = int(e1[1])   #fin section elfe 
        debut_e2 = int(e2[0])
        fin_e2 = int(e2[1])
        if not (fin_e1 < debut_e2 or fin_e2 < debut_e1) : # si les sections se superposent
            n+=1
    return n

assert superpose(lire_fichier("cleaning.txt")) == 794

print(sections(lire_fichier("cleaning.txt")))
print(superpose(lire_fichier("cleaning.txt")))