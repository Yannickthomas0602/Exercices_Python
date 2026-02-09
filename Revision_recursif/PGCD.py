# On rappelle que le PGCD de deux entiers a et b est égal au PGCD des deux entiers b et r où
# r est le reste de la division euclidienne de a par b. Écrire une fonction prenant en argument
# deux entiers a et b et renvoyant le PGCD de a et b. La fonction pourra être récursive.


def pgcd(a, b) -> int:
    if b == 0 : 
        return a
    else :
        r = a % b 
        return pgcd(b, r)

print(pgcd(9, 6))