from mis_funciones import nota_numerica

def media(*lista_notas):
    sum_notas = 0
    for nota in lista_notas:
        nota = nota.upper()
        valor = nota_numerica(nota)
        sum_notas += valor
        
    return sum_notas / len(lista_notas)