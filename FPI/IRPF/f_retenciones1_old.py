RANGOS = [0, 12450, 20200, 35200, 60000, 300000]
PORCENTAJES = [0, 19, 24, 30, 37, 45, 47]

RETENCIONES = [[0, 0], [12450, 19], [20200, 24], [35200, 30],
               [60000, 37], [300000, 45], [float('inf'), 47]
              ]


SITUACIONES = {
                '1': [0, 15947, 17100],
                '2': [15546, 16481, 17634],
                '3': [14000, 14516, 15063]
              }

def obtener_exencion(sit, nhijos):
    if nhijos > 2:
        nhijos = 2
    elif nhijos < 0:
        nhijos = 0
        
    if sit == '1':
        return SIT1[nhijos]
    if sit == '2':
        return SIT2[nhijos]
    if sit == '3':
        return SIT3[nhijos]
            
    return 0

def obtener_retencion_while(base):
    i = 0
    while i < len(RANGOS):
        if base <= RANGOS[i]:
            break
        
        i += 1
        
    return PORCENTAJES[i]

def obtener_retencion(base):
    for retencion in RETENCIONES:
        if base <= retencion[0]:
            return retencion[1]