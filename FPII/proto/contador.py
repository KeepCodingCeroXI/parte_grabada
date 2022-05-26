def creaContador(ini = 0):
    def clicks():
        nonlocal ini

        ini += 1
        return ini
    
    return clicks


def creaContadorReutilizable(ini=0):
    clicks = ini
    def reset(v):
        nonlocal clicks
        clicks = v

    def consulta():
        return clicks

    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            clicks += 1
            return clicks

        if 'reset' in kwargs:
            valor_inicial = kwargs['reset']
            reset(valor_inicial)
            return clicks
        elif 'consulta' in kwargs:
            return consulta()
        else:
            raise 'Método no permitido'

    return contador


class Contador():
    def __init__(self, ini=0):
        self.clicks = ini

    def click(self):
        self.clicks += 1
        return self.clicks

    def reset(self, v=0):
        self.clicks = v
        return self.clicks