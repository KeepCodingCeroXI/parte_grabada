from f_retenciones1 import *

# OBTENER DATOS DE ENTRADA
nif = input("NIF: ")
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

# OBTENER EXENCION

exencion = obtener_exencion(situacion, num_hijos)
sueldo_a_retener = sueldo - exencion
porcentaje = obtener_retencion(sueldo_a_retener)

# OBTENER RETENCION
    
monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

# MOSTRAR RESULTADOS
print("Sueldo anual: \t", sueldo)
print("Situacion:\t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Total anual:\t", monto_anual)
print()
print("Retencion mensual:", monto_mensual)

with open("rmensuales.dat", "a+") as data:
    print(data.tell())
    data.seek(0)
    tiene_datos = bool(len(data.read(1)))
    data.tell()
    if not tiene_datos:
        registro = "NIF\tSueldo Base\tSituacion\tBase a retener\tRetencion anual\tRetencion mensual\n"
        data.write(registro)
    registro = f"{nif}\t{sueldo}\t{situacion}\t{sueldo_a_retener}\t{monto_anual}\t{monto_mensual}\n"
    data.write(registro)
    
