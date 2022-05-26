# OBTENER DATOS DE ENTRADA
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))
gastos_generales = 2000
min_personal = 5550

# OBTENER EXENCION
exencion = 0
if situacion == '1':
    if num_hijos <= 0:
        exencion = 0
    elif num_hijos == 1:
        exencion = 15947
    else:
        exencion = 17100
        
if situacion == '2':
    if num_hijos <= 0:
        exencion = 15546
    elif num_hijos == 1:
        exencion = 16481
    else:
        exencion = 17634
        
if situacion == '3':
    if num_hijos <= 0:
        exencion = 14000
    elif num_hijos == 1:
        exencion = 14516
    else:
        exencion = 15063
        
sueldo_a_retener = sueldo - exencion - gastos_generales - min_personal

# OBTENER RETENCION
if sueldo_a_retener <= 12450:
    monto_anual = 12450 * 19 / 100
elif sueldo_a_retener <= 20200:
    monto_anual = 2365.50 + (sueldo_a_retener - 12450) * 24 / 100
elif sueldo_a_retener <= 35200:
    monto_anual = 4225.50 + (sueldo_a_retener - 20200) * 30 / 100
elif sueldo_a_retener <= 60000:
    monto_anual = 8725.50 + (sueldo_a_retener - 35200) * 37 / 100
elif sueldo_a_retener <= 300000:
    monto_anual = 17901.50 + (sueldo_a_retener - 60000) * 45 / 100
else:
    monto_anual = 125901.50 + (sueldo_a_retener - 300000) * 47 / 100
        
monto_mensual = monto_anual / 12

# MOSTRAR RESULTADOS
print("Sueldo anual: \t", sueldo)
print("Situacion:\t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Total anual:\t", monto_anual)
print()
print("Retencion mensual:", monto_mensual)
