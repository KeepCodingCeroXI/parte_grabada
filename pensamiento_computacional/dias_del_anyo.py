# introducir datos
dia = int(input("Dia: "))
mes = int(input("Mes: "))

# Contar los dias

contador_dias = 0
if mes == 1:
    contador_dias = dia
elif mes == 2:
    contador_dias = 31 + dia
elif mes == 3:
    contador_dias = 31 + 28 + dia
elif mes == 4:
    contador_dias = 31 + 28 + 31 + dia
elif mes == 5:
    contador_dias = 31 + 28 + 31 + 30 + dia
elif mes == 6:
    contador_dias = 31 + 28 + 31 + 30 + 31 + dia
elif mes == 7:
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + dia
elif mes == 8: 
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia
elif mes == 9: 
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia
elif mes == 10:
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia
elif mes == 11:
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia
else:
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia
    
# resultado
print("Es el dia:", contador_dias)
    