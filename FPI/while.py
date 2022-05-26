def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
        
    return notas[puntero]


num_notas = 0
sum_notas = 0

nota = input("Nota del alumno (nada para acabar): ")

while nota != "":
    num_notas += 1
    valor_nota = nota_numerica(nota)
    sum_notas += valor_nota
    
    nota = input("Nota del alumno (nada para acabar): ")
    
media = sum_notas / num_notas

print(media)
    
