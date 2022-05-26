dias = [31,28,31,30,31,30,31,31,30,31,30,31]

#pedir datos
dia = int(input("Dia: "))
mes = int(input("Mes: "))

#contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while compara_mes < mes - 1:
    #contador_dias = contador_dias + dias[compara_mes]
    contador_dias += dias[compara_mes]
    compara_mes += 1
    
contador_dias += dia

print("El dia es:", contador_dias)