suma = 0
pelota = "balon"

def sum_string(un_iterable):
    
    print(pelota)
    
    def mi_funcion_adentro_de_una_funcion():
        print("Soy una inner function")
        
    suma = ""
    for i in un_iterable:
        suma +=i
        
    mi_funcion_adentro_de_una_funcion()
    return suma
    
def sum_entero(un_iterable):
        suma = 0    
        for i in un_iterable:
            suma +=i
        return suma
    

print(sum_string(["1","h"]))


def welcome(nombre_ciudad):
    print(f"Hola bienvenido a {nombre_ciudad}")

def media_aritmetica(lista_numeros):
        suma = sum(lista_numeros)
        cantidad = len(lista_numeros)
        return (suma / cantidad) + 1
     
def media_aritmetica_dos(lista_numeros):
        return sum(lista_numeros) / len(lista_numeros)

def es_multiplo(a,b):
    return a % b == 0


assert es_multiplo(2,2)

assert media_aritmetica([1,2,3]) == 2.0








