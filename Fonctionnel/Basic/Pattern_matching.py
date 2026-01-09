def match_pattern(texte: str, pattern : str) -> list: 
    liste = []
    txt = len(texte)
    pat = len(pattern)
    for i in range(txt - pat + 1) : 
        if texte[i:i + pat] == pattern : 
            liste.append(i)
    return liste

assert match_pattern("AABAACAADAABAABA", "AABA") == [0, 9, 12]

print(match_pattern("AABAACAADAABAABA", "AABA"))