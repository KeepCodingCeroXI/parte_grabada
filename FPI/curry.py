def curry(func, *args, **kwargs):
    
    def res_func(*args_r, **kwargs_r):
        args_r = args + args_r
        kwargs_r.update(kwargs)
        return func(*args_r, *kwargs_r)
    
    return res_func


def multiplicar(a, b):
    if b <= 1:
        return a
    else:
        return a + multiplicar(a, b-1)
    

def fraccion_a_binario(n):
    