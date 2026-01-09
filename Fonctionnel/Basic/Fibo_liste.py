n=int(input("Entrez les n premiers termes de la suite :"))
def Fibo(n : int) -> list:
    liste = []
    if n <= 0:
        return "Si N = 0 alors la suite est vide"
    elif n == 1 : 
        return ""
    a = 0
    b = 1
    for _ in range(n): 
        liste.append(a)
        a = b
        b = a + b
    return liste
print(Fibo(n))

assert Fibo(5) == [0, 1, 2, 4, 8]