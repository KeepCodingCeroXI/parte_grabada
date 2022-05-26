def es_palindromo(cadena):
    cadena = cadena.replace(" ", "")
    cadena = cadena.lower()
    
    return cadena == cadena[::-1]

def saca_vocales(cadena):
    resultado = ""
    for letra in cadena:
        if letra in "aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ":
            resultado += letra
            
    return resultado