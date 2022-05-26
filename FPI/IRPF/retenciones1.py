import retenciones2021

# OBTENER DATOS DE ENTRADA
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

exencion = retenciones2021.calcula_exencion('1', 0)
base_a_retener = sueldo - retenciones2021.gastos_generales - retenciones2021.min_personal - exencion
retencion_mensual = retenciones2021.retencion_mensual(20000, '1', 0)

# MOSTRAR RESULTADOS
print("Sueldo anual: \t", sueldo)
print("Situacion:\t", situacion)
print("Base a retener:", base_a_retener)
print("Porcentaje:\t", retenciones2021.porcentaje(base_a_retener))
print("Total anual:\t", retencion_mensual*12)
print()
print("Retencion mensual:", retencion_mensual)

