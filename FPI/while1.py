def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
        
    return notas[puntero]


num_notas = 0
sum_notas = 0

nota = input("Nota o vacío para terminar: ")

while nota != "":
    nota = nota.upper()
    try:
        valor_nota = nota_numerica(nota)
        num_notas += 1
        sum_notas += valor_nota
    except IndexError:
        print("Nota", nota, "es incorrecta. Vuelva a intentarlo")
    
    nota = input("Nota o vacío para terminar: ")
    

if num_notas == 0:
    print("No se han introducido datos")
else:
    media = sum_notas / num_notas

    print("La media es:", media) 
    

