def pendu(mot: str) -> list: 
    n = 0 
    mot_trouve = False
    liste_mot = []
    i = 0
    while i < len(mot): 
        liste_mot.append("_")
        i += 1 
    while mot_trouve == False: 
        i=0 
        while i < len(liste_mot) : 
            print(liste_mot[i], end=" ")
            i+=1
        lettre = str(input("Entrez lettre :  "))
        n += 1 
        i = 0
        while i < len(mot) : 
            if mot[i] == lettre: 
                liste_mot[i] = lettre
            i += 1
        mot_trouve = True
        i = 0 
        while i < len(liste_mot) : 
            if liste_mot[i] == "_":
                mot_trouve = False
            i += 1
    print("Mot trouvé : ", mot)
    return "Nombre d'essais", n
n = pendu("bonjour")
print("nombre d'essais: ", n)
