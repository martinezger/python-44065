import json

a = '{"hola":"1"}'

a_dict = json.loads(a)


def sacar_el_ultimo(una_lista):
    if len(una_lista) > 0 and type(una_lista) == list: 
        return una_lista.pop()
    

def divi(a,b):
    
    if b == 0:
        result = "inderminado"
        
    try:
        result = a/b
    except ZeroDivisionError:
        result = "Division por Cero"
    except TypeError:
        result = "Solo se aceptan numeros"
    else:
        print("todo salio bien")
    finally:
        print("esto simpre se ejecuta")
    return result
    

assert divi("",1) == "Solo se aceptan numeros"
assert divi(0,13) == 0
assert divi(0, 0) == "Division por Cero"
assert divi(12,0) == "Division por Cero"
assert divi(12,2) == 6



def sumar_lista(una_lista):
    acum = 0
    try:
        for i in una_lista:
            acum += i
    except:
        print("Algo salio mal")
    else:
        print(acum)
    finally:
        result = []
        
    return result


def divi_dos(a,b):
    
    if b == 0:
        result = "inderminado"
        
    try:
        result = a/b
    except Exception as e:
        print(e)
        return None
    
    return result
    

