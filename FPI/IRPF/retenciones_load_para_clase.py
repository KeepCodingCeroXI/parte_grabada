with open("rmensuales.dat", "r") as data:
    lineas = data.read().splitlines()

if lineas:
    cabecera = lineas[0]
    registros = lineas[1:]

campos = cabecera.split('\t')

retenciones = []
for registro in registros:
    retencion = {}
    valores = registro.split('\t')
    for clave, valor in zip(campos, valores):
        retencion[clave] = valor
    retenciones.append(retencion)
        
for retencion in retenciones:
    print(retencion)