def obtener_exencion(situacion, num_hijos):
    """
    OBTENER EXENCION
    """
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
    
    return exencion

def obtener_retencion(sar):
    """
    OBTENER RETENCION
    """
    if sar <= 12450:
        porcentaje = 19
    elif sar <= 20200:
        porcentaje = 24
    elif sar <= 35200:
        porcentaje = 30
    elif sar <= 60000:
        porcentaje = 37
    elif sar <= 300000:
        porcentaje = 45
    else:
        porcentaje = 47
        
    return porcentaje
