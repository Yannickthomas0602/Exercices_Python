def fact(n : int) -> int: 
    resultat = 1
    i = 1
    while i <= n: 
        resultat *= i
        i+=1
    return resultat

assert fact(5) == 120

print(fact(5))