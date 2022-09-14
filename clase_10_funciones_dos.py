def sumar(*args): #args es la conveción, se puede poner lo que quieras, ej: *perro
    acumulador = 0
    if len(args) < 2:
      return 0
    
    for numero in args:
        acumulador += numero
    return acumulador


def join(*args, separador=" "):
    resultado = ""
    
    if not isinstance(separador, str):
        print("Separador no es String")
        return 

    for item in args:
        resultado += item + separador
    else:
        resultado = resultado[:-1]

    return resultado

def join(*args, separador=" ", borrar_ultimo=True):
    resultado = ""
    
    for item in args:
        resultado += item + separador
    else:
      if borrar_ultimo:
        resultado = resultado[:-1]

    return resultado


def una_funcion_con_kwargs(**kwargs): # **kwargs es la conveción, se puede poner lo que quieras, ej: **pepito
    print(type(kwargs))
    print(kwargs)

def print_datos_personales(**kwargs):
    print(f"Nombre:{kwargs.get('nombre')}, Apellido: {kwargs.get('apellido', '')}")


def suma(a, b):
    return a + b
    
def imprimr_resultado(func): 
    
    def funcion_interna(*args): 
        print("El resultado de la ejecucion de la funcion es:") 
        print(func(*args))
            
    return funcion_interna

@imprimr_resultado
def suma(a,b):
    return a + b

