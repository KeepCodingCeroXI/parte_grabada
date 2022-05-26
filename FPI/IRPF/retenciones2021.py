gastos_generales = 2000
min_personal = 5550

def calcula_exencion(situacion, num_hijos):
    exenciones = {
        '1': [0, 15947, 17100],
        '2': [15546, 16481, 17634],
        '3': [14000, 14516, 15063]
    }
    
    return exenciones[situacion][min(num_hijos, 2)]
    
def porcentaje(sueldo_a_retener):
    retenciones = [(12450, 19), (20200, 24), (35200, 30), (60000, 37), (300000, 45), (float('inf'), 47)]
    ix = 0
    while retenciones[ix][0] < sueldo_a_retener:
        ix += 1
        
    return retenciones[ix][1]

def retencion_mensual(bruto, situacion, num_hijos, num_nominas=12):
    exencion = calcula_exencion(situacion, num_hijos)
    sueldo_a_retener = bruto-gastos_generales-min_personal-exencion
    porc = porcentaje(sueldo_a_retener)
    monto_anual = sueldo_a_retener * porc / 100
    return monto_anual/num_nominas

if __name__ == '__main__':
    sueldo = float(input("Sueldo: "))
    situacion = input("Situacion (1/2/3): ")
    nh = input("Hijos: ")
    
    print( retencion_mensual(sueldo, situacion, int(nh)))