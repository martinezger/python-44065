import json
import os

cadena_formato_json = ' { "hola": "hi" } '
'''
json.load = es para cargar un archivo

json.loads = es para cargar un string
'''

cadena_formato_json_transformado_a_dict =json.loads(cadena_formato_json)
print(json.dumps(cadena_formato_json_transformado_a_dict))


archivo_formato_json = open("sample.json")
archivo_formato_json_transformado_a_dict = json.load(archivo_formato_json)
archivo_formato_json.close()
archivo_formato_json_transformado_a_dict["hola"] = "hi"

archivo_formato_json = open("sample.json", "w")
json.dump(archivo_formato_json_transformado_a_dict, archivo_formato_json)
archivo_formato_json.close()


with open("sample.txt", "w") as file:
    file.write("""hola
como
estas""")

with open("sample.txt", "w") as file:
    file.writelines(["hola" ,"como","estassss"])
    
    

def mi_funcion():
    1+1
    
def mi_funcion_dos(param):
    param+1
    
    
def mi_funcion_tres():
    return 1+1

def mi_funcion_cuatro(param):
    return param+1



def mi_funcion_cinco(param=0):
    return param

def mi_funcion_seis(param=0, param_dos=0):
    return param + param_dos


def mi_funcion_siete(*args):
    for i in args:
        print(i)
        
def mi_funcion_ocho(**kwargs):
    for k ,v in kwargs.items():
        print(f"{k}--{v}")

def mi_funcion_nueve(*args, **kwargs):
    for k ,v in kwargs.items():
        print(f"{k}--{v}")
    a = []
    for i in args:
        a.append(i)
    print(a)
    
    
def relancion(a,b):
    pass

assert relacion(20,1) == 1
assert relacion(1, 20) == -1
assert relancion(1,1) == 0



os.path.exists("sample.json")



