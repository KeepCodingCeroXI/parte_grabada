dias = [31,28,31,30,31,30,31,31,30,31,30,31]

def es_bisiesto(year):
    if year % 4 != 0:
    #if not year % 4 == 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True

#pedir datos
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anyo = int(input("Año: "))

#comprobar bisiesto
#if es_bisiesto(anyo) == True:
if es_bisiesto(anyo):
    dias[1] = 29    

#contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while compara_mes < mes - 1:
    #contador_dias = contador_dias + dias[compara_mes]
    contador_dias += dias[compara_mes]
    compara_mes += 1
    
contador_dias += dia

print("El dia es:", contador_dias)
