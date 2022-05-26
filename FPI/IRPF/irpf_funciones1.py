retenciones = [(12450, 19), (20200, 24), (35200, 30), (60000, 37), (300000, 45), (float('inf'), 47)]

situaciones = {'1': [0, 15947, 17100], '2': [15546, 16481, 17634], '3': [14000, 14516, 15063]}

def obtener_exencion(sit, nhijos):
    
    # nhijos = min(nhijos, 2)
    if nhijos > 2:
        nhijos = 2
  
    return situaciones[sit][nhijos]

def obtener_retencion(base):
    """
    Devuelve el porcentaje de retención de IRPF en función del valor de sar
    
    sar: float
    """
    for rango, retencion in retenciones:
        if rango >= base:
            return retencion


