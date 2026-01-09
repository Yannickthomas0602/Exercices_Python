def suppr_space(texte : str) -> str : 
    result = ""
    for val in texte : 
        if val != " " : 
            result += val 
    return result

def luhn(num_carte : str) -> bool :
    somme = 0 
    par_deux = False
    for i in range(len(num_carte) -1, -1, -1) : 
        n = int(num_carte[i])

        if par_deux is True : 
          n*=2
          if n >= 10 : 
              n -= 9 
        somme += n 
        par_deux = not par_deux
    return somme % 10 == 0 

liste = ["4137 8947 1175 5904","9724 8708 6", "4539 7043 5470 6091", "7992 7398 713"]

for val in liste : 
    print(val, "  ", "Valide" if luhn(suppr_space(val)) else "invalide")