def entero_a_binario(n: int) -> str:
    res = ""
    
    cociente = n // 2
    resto = n % 2
    n = cociente
    
    while n > 1:
        res += str(resto)
        cociente = n // 2
        resto = n % 2
        n = cociente    

    res += str(resto)
    res += str(n)
    res = res[::-1]
    
    return res


def fraccionario_a_binario(n: float, precision: int = 31) -> str:
    res = ""
    
    producto = n * 2
    parte_entera = int(producto)
    parte_decimal = producto - parte_entera
    n = parte_decimal
    contador = 1
    while n > 0 and contador < precision:
        res += str(parte_entera)
    
        producto = n * 2
        parte_entera = int(producto)
        parte_decimal = producto - parte_entera
        n = parte_decimal
        
        contador += 1

    res += str(parte_entera)
    
    return res


def a_binario(n: float, precision: int = 31) -> str:
    entero = int(n)
    parte_entera = entero_a_binario(entero)
    parte_decimal = fraccionario_a_binario(n - entero, precision)
    return f"{parte_entera},{parte_decimal}"
    
    
