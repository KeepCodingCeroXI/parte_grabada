def tacha(caracter, palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
    return ''.join(lpalabra)

def es_anagrama(p1, p2):
    for letra in p1:
        if letra in p2:
            p2 = tacha(letra, p2)
        else:
            return False
        
    return p2 == ""
def frecuencias(palabra):
    resultado = {}
    for letra in palabra:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
            
    return resultado

 
 
def es_anagrama_by_dict(p1, p2):
    fp1 = frecuencias(p1)
    fp2 = frecuencias(p2)
    return fp1 == fp2
