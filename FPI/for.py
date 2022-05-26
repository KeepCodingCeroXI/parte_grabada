def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    
    while letras[puntero] != letra:
        puntero += 1
        
    return notas[puntero]

def pedir_nota_correcta():
    valor = ""
    while valor == "":
        #nota = input("Nota: ").upper()
        nota = input("Nota: ")
        nota = nota.upper()
        
        try:
            valor = nota_numerica(nota)
        except IndexError:
            print("Nota", nota, "incorrecta. Vuelva a introducir")
            valor = ""
            
    return valor

def pedir_numero():
    valor = ""
    while valor == "":
        try:
            valor = int(input("Número de asignaturas: "))
        except ValueError:
            valor = ""
            print("Debe ser un número entero. Vuelva a introducirlo")
    return valor
    
        

num_notas = pedir_numero()
sum_notas = 0

for i in range(num_notas):
    valor = pedir_nota_correcta()

    sum_notas += valor
        
    
if num_notas == 0:
    print("No se han introducido datos")
else:
    media = sum_notas / num_notas
    print("La media es: ", media)
    
    
    
