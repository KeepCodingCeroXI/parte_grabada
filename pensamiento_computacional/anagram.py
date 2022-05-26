def isAnagram(p1, p2):
    listaComparacionLetras = []
    
    if len(p1) != len(p2):
        return False
    
    for c1 in p1:
        noAñadasFalse = False
        for c2 in p2:
            if c1 == c2:
                noAñadasFalse = True
                listaComparacionLetras.append(True)
                
        if not noAñadasFalse:
            listaComparacionLetras.append(False)
            
    return not False in listaComparacionLetras
            